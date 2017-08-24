Title: The start of a uClinux userland
Date: 2009-07-28 15:24
Author: green
Category: moxie
Tags: linux
Slug: the-start-of-a-uclinux-userland

Before we can start building [BusyBox][], we need a few more bits of
technology...

-   [uClibc][]: this is a popular embedded C library, like newlib, but
    used more often in Linux environments. I ported uClibc to the moxie
    core just like every other bit of software in this project: quickly!
    My strategy has always been to make things link as quickly as
    possible, and then sort out the details later. This seems to be a
    workable strategy in the presence of good testsuites and the like.
-   [elf2flt][]: this utility turns moxie ELF binaries into the ["Binary
    Flat" (BFLT) format][] currently required by my Linux port. The BFLT
    format is required because: (a) we don't have an MMU yet, so there's
    a single address space for the kernel and all applications, and (b)
    my moxie tools port doesn't yet support something like the [FR-V's
    FDPIC ABI][] that would allow for proper shared library support in
    the absence of an MMU. elf2flt ends up wrapping the installed
    linker, so builds actually produce BFLT binaries without any extra
    step.
-   a moxie-uclinux toolchain: I build this from the same sources as the
    moxie-elf toolchain, but with a sysroot containing the kernel and
    uClibc header files.

This is all built and committed to [moxiedev][], which means that you
can check it out and build it yourself with a single "ant build". I
haven't tried using it yet, and I know it will fail in its current
state. The next step is to build BusyBox with the moxie-uclinux
toolchain and create an [initramfs][] that we can link directly to the
kernel binary. That's when the debugging fun begins...

  [BusyBox]: http://www.busybox.net
  [uClibc]: http://www.uclibc.org
  [elf2flt]: http://cvs.uclinux.org/cgi-bin/cvsweb.cgi/elf2flt/
  ["Binary Flat" (BFLT) format]: http://www.beyondlogic.org/uClinux/bflt.htm
  [FR-V's FDPIC ABI]: ftp://ftp.redhat.com/pub/redhat/gnupro/FRV/FDPIC-ABI.txt
  [moxiedev]: http://moxielogic.org/wiki/index.php?title=MoxieDev
  [initramfs]: http://www.linuxfordevices.com/c/a/Linux-For-Devices-Articles/Introducing-initramfs-a-new-model-for-initial-RAM-disks/
