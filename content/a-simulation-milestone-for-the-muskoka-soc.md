Title: A simulation milestone for the Muskoka SoC!
Date: 2011-09-27 19:47
Author: green
Category: moxie
Tags: architecture, muskoka, SoC, verilog, wishbone
Slug: a-simulation-milestone-for-the-muskoka-soc

A moxie-based SoC had it's first successful simulation run today....

<center>
![gtkwave display of first code run][1]
</center>

Pretty exciting! So, here's what's happening...

The SoC, code named "Muskoka", has three main components: the moxie
core, a wishbone switch and a ROM device. The switch was easy to
implement, as I just have a single bus master (moxie), and a single
slave device (bootrom) for now. The boot ROM is populated with bits
generated by assembling the code below like so:

`   moxie-elf-as -o bootrom.x bootrom.s     moxie-elf-objcopy -O verilog bootrom.x bootrom.vh`

    .text
        xor $r0, $r0  # Zero out $r0
        xor $r1, $r1
        xor $r2, $r2
        xor $r3, $r3
        xor $r4, $r4
        inc $r0, 0x1  # Increment $r0 by 1
        inc $r1, 0x1
        inc $r2, 0x1
        inc $r3, 0x1
        inc $r4, 0x1
        inc $r0, 0x1
        inc $r1, 0x1
        inc $r2, 0x1
        inc $r3, 0x1
        inc $r4, 0x1
        inc $r0, 0x1
        inc $r1, 0x1
        inc $r2, 0x1
        inc $r3, 0x1
        inc $r4, 0x1

The moxie core itself is has 4 pipeline stages: Fetch, Decode, Execute
and Write. The Fetch stage is probably the most complicated at this
point. Remember that moxie has both 16- and 48-bit instructions.
However, we're fetching instruction memory from the ROM device 32-bits
at a time. The fetch logic feeds these 32-bits into an instruction queue
and pulls out the right number of bits at the other end, depending on
the instruction about to be decoded.

So far only NOP, XOR and INC have been implemented, and there's no
pipeline hazard detection logic, but careful analysis of the simulation
dumps in gtkwave show that everything is finally starting to work. Baby
steps...

As usual, everything has been committed to [moxiedev][] on github.

  [1]: http://moxielogic.org/blog/wp-content/uploads/2011/09/gtkwave20110927-300x204.png
  [moxiedev]: http://github.com/atgreen/moxiedev "moxiedev"