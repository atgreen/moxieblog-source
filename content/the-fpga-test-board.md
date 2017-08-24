Title: The FPGA test board
Date: 2010-08-18 14:03
Author: green
Category: moxie
Tags: de2, fpga
Slug: the-fpga-test-board

I picked up a lightly used FPGA development board from craigslist today.
It's the [Altera DE2][] board with a Cyclone II FPGA.

<center>
!["The DE2\\'s Cyclone II "][1]
</center>

There are a few nice things about this board...

-   It's loaded with real and useful peripherals: 16x2 LCD Panel, VGA
    DAC, lots of LEDs, RS232, IrDA, PS/2, USB, 100/10Mbs Ethernet, audio
    codec, NTSC TV decoder, SD card connector, etc, etc. This means I
    can focus on the moxie microarchitecture, and not worry about
    building a full feature rich SoC.
-   Altera's Quartus II software runs on Linux
-   It was relatively cheap - \$200

When I got home I was happy to discover that the board actually powers
on and the appropriate LEDs blink. You can never be sure with used
hardware!

As for the Quartus software... I'm running Fedora 13 x86-64. This isn't
a supported OS for them but I'm hoping it will work since they do
support RHEL5. Quartus appears to be a 32-bit binary, so I had to go
through a tedious process of installing missing 32-bit libraries -
something that could have been avoided if they would simply package this
thing in an RPM. The good news is that after installing the appropriate
libraries, it does appear to start up.

More as it happens...

  [Altera DE2]: http://www.altera.com/education/univ/materials/boards/unv-de2-board.html
  [1]: http://moxielogic.org/blog/wp-content/uploads/2010/08/P1230549-300x225.jpg

