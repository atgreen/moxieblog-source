Title: The Moxie Game Console?
Date: 2014-01-11 06:06
Author: green
Category: moxie
Tags: marin, NetHack, Nexys3, RTEMS
Slug: the-moxie-game-console

Ok, not quite, but [Krister Lagerström][] recently did something cool..

<center>
![nethack][1]
</center>

That's [NetHack][] ported to [RTEMS][] running on the moxie based [Marin
SoC][].

It runs on QEMU, via
"`qemu-system-moxie --nographic --machine marin --kernel nethack.elf`",
or on FPGA hardware. I tested with a Nexys 3 Spartan-6 board by simply
converting it to an screcord file and sending it via the serial port to
the hardware's boot loader.

Krister implemented the Marin BSP for RTEMS, then ported ncurses and
nethack to moxie-rtems. Like many programs with a UNIX heritage, NetHack
reads data files from a local file system. RTEMS solves that by
providing a simple in-memory filesystem you can initialize with a tar
file and link to your ELF executable.

For my part, I had to fix a couple of QEMU bugs and point the
moxie-cores tools build scripts to staging git repos until the bugs are
fixed upstream. As usual, everything should be here:
<http://github.com/atgreen/moxie-cores>.

Thank you, Krister, and I'm looking forward to the other cool things you
have planned!

  [Krister Lagerström]: https://github.com/kl7107 "Krister"
  [1]: http://moxielogic.github.io/images/nethack.png
  [NetHack]: http://www.nethack.org/ "NetHack"
  [RTEMS]: http://rtems.org "RTEMS"
  [Marin SoC]: http://github.org/atgreen/moxie-cores "Marin SoC"
