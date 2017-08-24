Title: A Really Tiny GDB Remote Protocol Stub
Date: 2013-11-28 18:44
Author: green
Category: moxie
Tags: gdb, marin
Slug: a-really-tiny-gdb-remote-protocol-stub

I recently trimmed the Marin SoC's on-chip memory down to 4k. The
existing firmware for downloading srecord programs into external RAM for
execution was taking up about 2k. With 2k to spare, I was wondering if
you could fit a GDB remote protocol stub in there as well. It turns out
that you can! Here is the code for tinystub.c:
<https://raw.github.com/atgreen/moxie-cores/master/firmware/tinystub.c>.

With this stub you can load programs into the target device, examine
memory, run programs and even set breakpoints (I had to finally
implement BRK in the moxielite core for this).

A full tinystub executable (with startup code, etc), is about 2200 bytes
of moxie code. This means I can easily merge it with the existing
firmware, allowing people to either download an srecord program or
connect to the device with moxie-elf-gdb. I believe everything is in
place now to support running the GCC testsuite on hardware (dejagnu will
use gdb to download an execute test programs).
