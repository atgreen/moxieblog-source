Title: MoxieLite in Action
Date: 2012-09-22 04:40
Author: green
Category: moxie
Tags: fpga, gcc, MoxieLite, vga, Xilinx
Slug: moxielite-in-action

<center>
![][]
</center>

Brad Robinson just sent me this awesome shot of [MoxieLite][] in action.
His Xilinx Spartan-6 FPGA based SoC features a moxie core handling VGA
video, keyboard and FAT-on-flash filesystem duties using custom firmware
written in C. This is all in support of a second z80-based core on the
same FPGA used to emulate an '80s era computer called the [MicroBee][].
Those files in the listing above are actually audio cassette contents
used to load the MicroBee software. The moxie core is essentially a
peripheral emulator for his final product.

Keep up the great work, Brad!

The most recent [compiler patch][] was the addition of `-mno-crt0`,
which tells the compiler not to include the default C runtime startup
object at link time. This is common practice for many embedded projects,
where some system specific house keeping is often required before C
programs can start running. For instance, you may need to copy the
program's `.data` section from ROM into RAM before jumping to `main()`.

I'm going back to my pipelined moxie implementation. Last I looked I had
to move memory reads further up the pipeline...

  []: http://moxielogic.org/images/MoxieLite-400.jpg "First MoxieLite Shot"
  [MoxieLite]: https://github.com/toptensoftware/MoxieLite "MoxieLite"
  [MicroBee]: http://en.wikipedia.org/wiki/MicroBee
  [compiler patch]: http://gcc.gnu.org/ml/gcc-patches/2012-09/msg01572.html
