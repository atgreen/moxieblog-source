Title: The Moxie Linux port
Date: 2009-07-23 03:50
Author: green
Category: moxie
Tags: linux
Slug: the-moxie-linux-port

I've just checked the start of the kernel port into [moxiedev][].
Running "ant build" will produce tools, simulators, u-boot and now a
vmlinux you can run with moxie-elf-run or in gdb. It crashes on startup
right now, but that's to be expected. I just got it to the point where
it links. More to come...

  [moxiedev]: http://www.moxielogic.org/wiki/index.php?title=MoxieDev
