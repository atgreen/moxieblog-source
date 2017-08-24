Title: Notes on a novel in-game CPU: the dcpu-16
Date: 2012-04-09 07:35
Author: green
Category: moxie
Tags: architecture, binutils, dcpu-16, gcc, gdb
Slug: notes-on-a-novel-in-game-cpu-the-dcpu-16

The hacker behind the [Minecraft][] phenomena, Notch, is working on his
[next game][], most likely another hit. This one is interesting in that
it includes an in-game 16-bit processor called the dcpu-16. Details are
sparse, but it seems as though gamers will use this processor to control
spacecraft and play in-game games. The dcpu-16 spec is currently
available at <http://0x10c.com/doc/dcpu-16.txt>, and in the few days
since its release there are already many community produced assemblers
and emulators.

Like moxie, it's a load-store architecture with variable width
instructions (16 to 48 bits long). But the dcpu-16's 16-bitness is
pervasive. There are 8 16-bit registers, and the smallest addressable
unit of memory is a 16-bit word. There are only about 16 unique opcodes
in the 16-bit instruction, which means there's room for 2 6-bit
operands. With only 8 registers, a 6-bit operand can encode multiple
addressing modes (direct, indirect, offset, etc) and still have room for
small literal values.

If you poke around github you'll find the start of a [llvm backend][] as
well as a [tcc][] port. I haven't looked into these compilers, but a C
ABI for the dcpu-16 would certainly be unusual to most developers. You
would likely have a 32-bit long, but char, short and int would all be 16
bits.

As far as GNU tools go, a binutils port would be pretty straight
forward. I created a branch in [moxiedev][] to try my hand at a dcpu-16
binutils port. It's not very well tested, but gas, ld, objdump, etc all
appear to work as advertised. All instructions with immediate operands,
whether literal values or computed by linker relocations, are encoded in
their long form. Taking advantage of the smaller encodings will require
linker relaxation work. It's not rocket science, but more work than the
couple of hours I was willing to put into it. There appears to be one
bug in GNU ld related to handling relocations for ELF targets where the
smallest addressable memory value is 16 bits vs 8. I worked around it by
making one small non-portable change to the target independent linker
code.

I think GDB should be fairly straight forward as well. For most real
targets GDB will want to insert breakpoint instructions in the text of a
program, and it wants that instruction to be the same size as the
smallest instruction available on the target. Alas, the dcpu-16 has no
breakpoint instruction, 16-bit or othwerwise, so the simulator will have
to include special hardware breakpoint emulation logic. My suggestion is
to repurpose some of the 16-bit illegal instruction encodings. For
instance, the ISA allows for nonsensical instruction like this:

      SET 5, 6

This means set the literal value 5 to 6. Setting a literal value makes
no sense, and the spec currently says that these instructions are
silently ignored. Rather than ignore them, you could use this class of
instruction as special software interrupt/breakpoint/trap instructions
like moxie's `swi`.

A GCC port would be more challenging. It's definitely possible, but
would stretch GCC outside of its comfort zone. You'd end up excercising
bits of the compiler that aren't normally tested, and I imagine would
end up spending a lot of time debugging some of the darker recesses of
the compiler code. Best of luck to the brave soul who tries this!

I'm very curious to see how this all plays out. Given the massive
success of Minecraft, I wouldn't be surprised if we see an app store for
in-game dcpu-16 based games. Good luck to Notch and the team at Mojang.

  [Minecraft]: http://www.minecraft.net/
  [next game]: http://0x10c.com/
  [llvm backend]: https://github.com/krasin/llvm-dcpu16
  [tcc]: https://github.com/Wallbraker/DCPU-TCC
  [moxiedev]: https://github.com/atgreen/moxiedev
