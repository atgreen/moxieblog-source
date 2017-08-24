Title: Adding a Real Time Clock
Date: 2009-03-17 15:38
Author: green
Category: moxie
Tags: bsp, qemu
Slug: adding-a-real-time-clock

After a UART, one of the most useful and interesting peripherals you can
add to a board is a Real Time Clock (RTC). Qemu comes with a simulation
of Freescale's [MC146818][] RTC chip. Adding it to our qemu-defined
board was as simple as....

       rtc_mm_init(0x400, 0, 0, 0);

This makes the MC146818 available as a memory mapped port at `0x400` on
our target board. The simplest way to use this is to implement a qemu
specific `time()` function in the qemu BSP that pulls the current time
from the `0x400`-mapped port. I won't include the code here, but it's
quite simple, and found in  
`moxiedev/src/libgloss/moxie/qemu-time.c`. Now functions like
`gettimeofday()` work as expected, making the whole platform a little
more real.

After an RTC, I think the next most interesting peripheral is an
interrupt controller, but this will require more thought about the
system architecture and how moxie will handle exceptions.

  [MC146818]: http://www.freescale.com/files/microcontrollers/doc/data_sheet/MC146818.pdf
