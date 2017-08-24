Title: And time ticks on...
Date: 2013-03-29 20:12
Author: green
Category: moxie
Tags: marin, MoxieLite, qemu, RTEMS, SoC
Slug: and-time-ticks-on

The interrupt controller [is working now][], as is the timer and my
exception handling firmware. So now I'm able to write a basic stop-watch
application, where the 7-segment display simply increments the count
every second. Yes, this sounds basic, but there's a lot of complexity
under the hood! This is all with the MoxieLite-based Marin SoC. Next up:
one of the following...

​1. Finish the hardware GDB remote protocol handler, or  
2. Implement a Marin board emulator in QEMU, or  
3. Add support for external RAM (I'm currently just using limited FPGA
BRAM), or  
4. Add interrupt support and timer ticks to RTEMS, or  
5. Hook up the bus watchdog to the processor (should this go through
the interrupt controller? Or directly to the core?)

We shall see....

  [is working now]: https://github.com/atgreen/moxie-cores/commit/0e44d0f29a2f05ef7f99fb1fc5d670d7f99d7c0b
