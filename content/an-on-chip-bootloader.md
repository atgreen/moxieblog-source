Title: An On-Chip Bootloader
Date: 2013-05-06 02:25
Author: green
Category: moxie
Tags: marin, newlib, u-boot
Slug: an-on-chip-bootloader

Good news: we can access external memory! The logic for my pseudo-static
RAM controller is working, and big programs can finally run on hardware.

You may recall that I had previously only been accessing fake memory
that was configured directly out of limited FPGA resources. I could
squeeze a tiny C program in there, but not use anything like newlib, the
embedded C runtime library. This new memory controller lets the
moxie-based Marin SoC access 16MB of external RAM on the Nexys3 board.

When we were limited to on-chip resources, the C binary would be coupled
with the synthesized logic and loaded directly into the FPGA. This means
any changes to the code meant resynthesizing the logic to rebuild the
FPGA bitstream (I think there are ways around this, but I never got
there with my work-flow). Now that I have access to external RAM, I can
separate my code from my logic.

The trick is to use an on-chip bootloader - code that is loaded with the
FPGA bitstream as described above. It does some basic hardware
initialization, and sends this message to the serial port:

` MOXIE On-Chip Bootloader v1.0 Copyright (c) 2013 Anthony Green `

Waiting for S-Record Download...  
</code>

At which point I can send any program I like over my laptop's serial
port in the form of an S-Record ASCII file. This generally looks
like...  

` $ moxie-elf-gcc -Os hello.c marin.S -T../../moxie-marin.ld -o hello.elf -lnosys $ moxie-elf-objcopy -O srec --srec-forceS3 hello.elf hello.srec $ cat hello.srec > /dev/ttyUSB1`

And then, back on the Nexys3 serial port I see:  
` Jumping to code at 0x30000000. Hello World!`

A couple of things can happen now:

-   with a little bit of dejagnu hacking, we can get the GCC testsuite
    to run directly on hardware. The simple thing here is to just have
    libgloss' \_exit() jump back to the on-chip bootloader @ 0x1000.
-   test the "stage-2" bootloader, u-boot. U-Boot was one of the first
    programs I ever ported to moxie. I've run it on the simulator, but
    never on hardware.

As usual, everything is in the moxie-cores github repo here:
<http://github.com/atgreen/moxie-cores>.
