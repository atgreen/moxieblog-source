Title: An ELF Machine Number for Moxie
Date: 2015-01-09 15:21
Author: green
Category: moxie
Tags: gcc
Slug: elf-machine-number

Moxie was assigned an official ELF machine number this week!  You can
check it out here:
[http://www.sco.com/developers/gabi/latest/ch4.eheader.html](http://www.sco.com/developers/gabi/latest/ch4.eheader.html).

All ELF files start with a header describing properties of the object
at hand.  One of the most important properties is the 'machine' type.
The machine type identifies the basic architecture for which the given
binary is relevant.  It is represented as a 16-bit integer, so, for
instance, MIPS is 3, ARM is 40, AVR32 is 185, and now, I'm happy to
say, Moxie is 223.

Linkers, loaders, and similar tools examine the machine number to make
sure they're working with the right kinds of files.  This saves us
from linking SH4 and Sparc objects into x86_64 executables.

Until recently the Moxie GNU binutils port had been using a temporary
machine number of 0xFEED.  Every new architecture, however, should get
an official number assigned by the System V gABI maintainers.  Just
send a nice email requesting the number assignment to registry@sco.com
and they'll increment their most recent number and add you to the
list.

If you look at GNU binutils you'll see that many ports, including
Moxie, live for quite some time using arbitrary machine number values
unlikely to conflict with the slowly incrementing official numbers.
Others, like the FTDI FT32 port, get their numbers (222) assigned in
advance of port submission.  If you go the same route I did, you'll
see that binutils has a mechanism whereby you can identify the main
machine number (223) as well as alternative numbers (0xFEED) to ease
in the transition.  This is all that needed doing:
[https://sourceware.org/ml/binutils/2015-01/msg00105.html](https://sourceware.org/ml/binutils/2015-01/msg00105.html).

Happy Hacking!
