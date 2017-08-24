Title: QEMU 1.5 includes Moxie support
Date: 2013-05-21 04:16
Author: green
Category: moxie
Tags: marin, qemu, u-boot
Slug: qemu-1-5-includes-moxie-support

QEMU 1.5 was just released the other day, and in the ["And much
more..."][] category I'm happy to say that it includes Moxie support!

This release contains basic Moxie core support, with the imaginary
"moxiesim" board support. I have some local changes that provide Marin
SoC emulation, and can run the [on-chip bootloader I recently wrote
about][]. In this example, for instance, we're sending the u-boot
bootloader program in srecord format to qemu's emulated serial port on
stdin. It looks just like the real hardware does...


    $ cat ~/u-boot.srec | qemu-system-moxie --machine marin --kernel bootrom.elf --nographic
    MOXIE On-Chip Bootloader v1.0
    Copyright (c) 2013 Anthony Green 

    Waiting for S-Record Download...
    Jumping to code at 0x30000000.
    SDRAM :
        U-Boot Start:0x30000000
    Using default environment

    U-BOOT for "marin"
    => 

We're just a few baby steps away from being able to do really cool
things!

  ["And much more..."]: http://lists.nongnu.org/archive/html/qemu-devel/2013-05/msg02557.html
  [on-chip bootloader I recently wrote about]: http://moxielogic.org/blog/?p=738
