Title: Running a C Program on the Marin SoC
Date: 2012-11-15 21:10
Author: green
Category: moxie
Tags: fpga, gcc, marin, newlib, Nexys3, SoC
Slug: running-a-c-program-on-the-marin-soc

I've just committed the bits required to run a [C program][] on the
Marin SoC.

Rather than hook up the Nexys3 external RAM module, I'm using extra
space on the FPGA itself for RAM. Most of the hard work was sorting out
the [linker script][] magic required to generate an appropriate image.

I've also added a [UART with 1k hardware FIFO transmit and receive
buffers][]. The 1k is probably overkill, so I'll likely shrink them once
everything else is working.

I've moved all memory mapped IO devices up to 0xF0000000. So, for
instance, the 7-segment display LED is at 0xF0000000, and the UART
transmit register is at 0xF0000004. I'll just keep going from there.

Next comes libgloss hacking to map stdout/stdin to the UART (which I
talk to with minicom on my Linux box). We're very close to "Hello World"
now!

  [C program]: https://github.com/atgreen/moxie-cores/blob/master/firmware/mdata.c
  [linker script]: https://github.com/atgreen/moxie-cores/blob/master/soc/marin/moxie-marin.ld
  [UART with 1k hardware FIFO transmit and receive buffers]: https://github.com/atgreen/moxie-cores/tree/master/cores/uart
