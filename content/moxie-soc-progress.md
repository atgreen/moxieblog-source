Title: Moxie SoC Progress
Date: 2012-11-10 05:23
Author: green
Category: moxie
Tags: fpga, marin, MoxieLite, Nexys3, SoC, u-boot, wishbone, Xilinx
Slug: moxie-soc-progress

Time for a quick update!

<center>
<iframe width="560" height="315" src="http://www.youtube.com/embed/86-OkQcXEes" frameborder="0" allowfullscreen></iframe>
</center>

"Marin" is the name of my test SoC consisting of a [wishbone][] wrapped
75Mhz big-endian MoxieLite bus master, along with two slave devices:
embedded ROM and the Nexys3's 7-segment display. So, right now I can
write some code into FPGA embedded ROM to manipulate the display. For
example...

            .text
	    .p2align        1
            .global MarinDisplayTest

            .equ BIG_ENDIAN,1

            # This is where 7-segment display is mapped to memory
            .equ DISPLAY_ADDR,0x00100000

    MarinDisplayTest:
            ldi.l   $r1, 0x1234
            ldi.l   $r3, 0x0
    loop:   sta.s   DISPLAY_ADDR, $r1
            dec     $r1, 1
            ldi.l   $r2, 5000000
    delay:  dec     $r2, 1
            cmp     $r2, $r3
            bne     delay
            jmpa    loop

This displays a countdown on the hex display starting at 1234.

Here's what I think will be next:

-   I need to be able to access RAM, which means implementing a module
    to support the Nexys3's [CellularRAM][] device and wrapping that up
    as a wishbone slave.
-   Once I can access RAM, I can test C compiler output, but only small
    code that I can embed into the FPGA's ROM.
-   Next comes a UART wishbone slave so I can talk to it over the
    microusb serial port from my Linux host. I'll need to hack up
    libgloss to map I/O to my memory-mapped UART.
-   One of the annoying things about this Xilinx toolchain is that
    AFAICT Digilent doesn't provide the tool you need for programming
    memory (Flash, RAM, or otherwise) from your Linux host. So I plan on
    writing some ROMable firmware to download code (srecords?) over the
    UART (xmodem?) to program memory. This is the point at which we
    should be able to run larger programs. I already have a u-boot port,
    so I think that will be first on my list.

It's great to have Brad Robinson's MoxieLite implementation for Marin.
It's very small but can still run at quite a clip. Once the surrounding
infrastructure is working, however, I'm going to get back to Muskoka,
which is my 4-stage pipelined moxie SoC to see if I can crank up the
MHz.

As usual everything is in github. However, the HDL cores and SoC designs
are no longer embedded in the moxiedev tree. They're in a new top-level
git repo called moxie-cores. Check it out here:
<http://github.com/atgreen/moxie-cores>

  [wishbone]: http://en.wikipedia.org/wiki/Wishbone_(computer_bus)
    "wishbone"
  [CellularRAM]: http://www.micron.com/products/dram/psram-cellularram
    "CellularRAM"
