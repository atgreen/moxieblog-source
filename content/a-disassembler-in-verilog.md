Title: A Disassembler in Verilog
Date: 2009-06-22 18:55
Author: green
Category: moxie
Slug: a-disassembler-in-verilog

I've been playing around a little more with verilog. Here's a mostly
complete moxie [disassembler module][] written in verilog.

And here's a little [driver][] for it. The driver reads a hex dump file
into an array representing memory. On every clock cycle it updates the
instruction and data output registers and increments the program
counter. The disassembler samples those values on every cycle, and tells
the driver how far to increment the PC. Pretty basic stuff!

    $ moxie-elf-gcc -o hello.x hello.c -Tsim.ld
    $ moxie-elf-objdump hello.x -O verilog hello.vh
    $ iverilog test-iprinter.v ../../iprinter.v
    $ ./a.out
            ldi.l   $sp ,   0x00400000
            ldi.l   $fp ,    0x00000000
            dec     $sp ,     12
            ldi.l   $r0 ,    0x000128b4

etc etc etc

Nothing too impressive really. I've stuck this test code in a directory
hierarchy that would be useful for dejagnu, as I plan on using dejagnu
for regression testing the various HDL modules.

  [disassembler module]: http://github.com/atgreen/moxiedev/blob/fb57efc73e47e451f18951d274c41ccda337c112/moxie/rtl/verilog/iprinter.v
  [driver]: http://github.com/atgreen/moxiedev/blob/fb57efc73e47e451f18951d274c41ccda337c112/moxie/rtl/verilog/testsuite/moxie.modules/test-iprinter.v
