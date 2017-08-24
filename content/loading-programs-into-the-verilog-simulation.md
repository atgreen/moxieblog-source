Title: Loading programs into the verilog simulation
Date: 2009-04-22 13:38
Author: green
Category: moxie
Tags: binutils, gcc, newlib, verilog
Slug: loading-programs-into-the-verilog-simulation

The moxie newlib port was [just accepted][]. The GCC port will take a
little longer to review, but I hope that it will get accepted early next
week. Already there has been some useful feedback resulting in a few
improvements. For instance, the moxie libgcc.a now provides the soft-fp
floating point emulation library instead of the fpbit one. Apparently
it's harder/better/faster/stronger, and other ports are starting to
adopt it. See the ["Improving Software Floating Point Support" paper][]
from the 2006 GCC Summit Proceedings</a> for details.

<object width="425" height="344">
<param name="movie" value="http://www.youtube.com/v/K2cYWfq--Nw&amp;hl=en&amp;fs=1"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param>

<embed src="http://www.youtube.com/v/K2cYWfq--Nw&amp;hl=en&amp;fs=1" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="344">
</embed>
</object>

On the verilog front, I have what I believe is a first pass at the
Instruction Fetch and Decode (IF/ID) units. In order to test these, you
actually need real code loaded into the simulated memory. Verilog
provides a handy function, $readmemh(), that sucks ASCII hex codes from
a text file into a register array (fake memory). The trick is that the
input file has to be in a very special format. To that end, I've written
a new BFD write-only backend called 'verilog' that generates this hex
dump output. So now...  

      $ moxie-elf-gcc -o hello.x hello.c
      $ moxie-elf-objcopy -O verilog hello.x hello.vh

...produces a useful hello.vh, which verilog can load directly
into memory like so...

    module memory();
      reg [7:0] my_memory [0:64000];
      initial begin
        $readmemh("hello.vh", my_memory);
      end
    endmodule;

I just [submitted this to the binutils list for review][]. Keep your
daft fingers crossed!

And this means I'm just about to start testing my IF/ID units on real
code.

  [just accepted]: http://sourceware.org/ml/newlib/2009/msg00520.html
  ["Improving Software Floating Point Support" paper]: http://ols.fedoraproject.org/GCC/Reprints-2006/sidwell-reprint.pdf
  [submitted this to the binutils list for review]: http://sourceware.org/ml/binutils/2009-04/msg00321.html
