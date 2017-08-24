Title: Das U-Boot on moxie!
Date: 2009-04-02 16:28
Author: green
Category: moxie
Tags: u-boot
Slug: das-u-boot-on-moxie

My moxie port of [U-Boot][], the Universal Boot Loader, has started
working!

    $ qemu-system-moxie -nographic -kernel u-boot
    SDRAM :
            U-Boot Start:0x00001000
    Using default environment

    U-BOOT for "moxiesim"

    => version

    U-Boot 2009.03-rc2-00013-gefb4734-dirty (Apr 02 2009 - 20:07:32)
    => printenv
    bootargs=root=romfs
    baudrate=38400
    hostname="moxiesim"

    Environment size: 55/4092 bytes
    => 

It's pretty amazing to have an interactive app running on qemu now.
U-Boot is using the serial port for console communications (we added the
UART to qemu [a few blog entries ago](qemu-says-hello-world.html)). I haven't added any ethernet
device yet, so all of the networking is configured out for now. There's
not even a timer device, so the sleep command doesn't work. However,
this is still a huge step forward.

I haven't decided yet if the U-Boot port will live in [MoxieDev][]. It's
already quite huge, and this would add another 130MB or so. I'll sleep
on it.

  [U-Boot]: http://www.denx.de/wiki/U-Boot
  [MoxieDev]: http://moxielogic.org/wiki/index.php?title=MoxieDev
