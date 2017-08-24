Title: Everything is relative (finally!)
Date: 2009-06-07 17:57
Author: green
Category: moxie
Tags: architecture, binutils, gcc, u-boot
Slug: everything-is-relative-finally

The Moxie ISA still needs quite a bit of tuning. Take branches, for
instance. A `beq` instruction currently encoded [like so][]...  

    `00001111xxxxxxxx iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`
  
...where the "`x`"s represent "don't care" bits, and "`i`"s are a
32-bit absolute branch target. That's right -- branch targets are not PC
relative! This is hugely wasteful.

I've finally got around to fixing this. Here's how I did it...

1.  I recoded all branch instructions as "Form 3" instructions, and
    tweaked the as-of-yet unused Form 3 encodings so they look like
    this:  

    >       FORM 3 instructions start with a bits "11"...                                 
    >                                                                                     
    >         11oooovvvvvvvvvv                                                            
    >         0              F                                                            
    >                                                                                     
    >        oooo         - form 3 opcode number                                          
    >        vvvvvvvvvv   - 10-bit immediate value. 

    This gives us 16 opcodes with a 10-bit immediate value. There are
    only 9 branch instructions, so we have a bit of room left in the
    Form 3 opcode space.

2.  I introduced a new 10-bit PC-relative Moxie relocation in BFD. This
    tells the linker and friends how to process PC-relative relocations.
3.  I hacked the assembler to generate these new relocations instead of
    simply emitting a 32-bit absolute address.
4.  I hacked the disassembler to print the new Form 3 instructions out
    nicely.
5.  Finally, I taught the compiler how to emit valid branch
    instructions. It's not that they look any different now; it's just
    that you need to worry about branch targets that exceed our 10-bit
    range. Actually, we have an 11-bit range because we know that all
    instructions are 16-bit aligned. This lets us drop the bottom bit
    from the encoding since we know it will always be `0`.  
    An 11-bit range lets us branch about 1k backwards to 1k forwards.
    If the compiler detects that a branch target is out of range, we
    want it to do something like the following transformation...

    >         beq    .FAR_TARGET

    ...becomes...

    >         bne    . + 8
    >         jmpa   .FAR_TARGET

    The "`bne .+8`" line means branch forward 8 bytes from the current
    PC. This would skip the unconditional jump to `.FAR_TARGET` (a
    6-byte instruction + 2-bytes for the branch = 8). Note that we have
    to reverse the logic from "`beq`" to "`bne`" for this to make sense.

    This is only possible if GCC can tell how far away the branch
    targets are. Fortunately, we're able to annotate instructions in the
    machine description file (`moxie.md`) with their length; currently
    either 2 or 6 bytes long. GCC then processes these annotations to
    determine branch distances.

    Now that we know branch distances at compile time, the compiler can
    do smart instruction selection to deal with out-of-range branches.
    The changes were quite simple and limited to the .md file in the
    backend.

The savings after this ISA change are substantial. For instance, the
consumer\_jpeg\_c benchmark in [MoxieDev][] is more than 15% smaller
when we use PC-relative branches! The [u-boot][] binary, on the other
hand, is "only" 7% smaller.

I hope to commit these changes to SRC and GCC once the GCC port is
merged upstream. Fingers crossed...

  [like so]: http://www.moxielogic.org/wiki/index.php?title=Instruction_Set#beq
  [MoxieDev]: http://www.moxielogic.org/wiki/index.php?title=MoxieDev
  [u-boot]: http://www.denx.de/wiki/U-Boot
