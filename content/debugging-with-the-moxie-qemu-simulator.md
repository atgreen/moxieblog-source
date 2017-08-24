Title: Debugging with the moxie qemu simulator
Date: 2009-03-14 06:58
Author: green
Category: moxie
Tags: gdb, qemu
Slug: debugging-with-the-moxie-qemu-simulator

I've finally cracked the gdb+qemu puzzle, so now we can debug code
running on the qemu moxie simulator!

The last little gotcha was that the simulated $pc wasn't being updated
after single-stepping. This will get you nowhere fast! But it's all
fixed now, and here's how it works...

`$ qemu-system-moxie -s -S -kernel hello.x`

This tells qemu to load our hello world program, hello.x. The "-s"
option tells it to wait for a connection from GDB on port 1234. The -S
option tells it to freeze on startup, and wait for a "continue" command
from the debugger.

Now, in a different terminal, fire up moxie-elf-gdb on hello.x and
connect to qemu like so:

`(gdb) target remote localhost:1234`

GDB and qemu should be talking now, and the debugger will report that
the sim is waiting on `__start`, the entry point to our hello.x ELF
file. Put a breakpoint on `main`, and hit 'c' to continue. You should be
debugging as usual now. I normally run moxie-elf-gdb within emacs in
order to get a nice UI, but invoking it from ddd or Eclipse should work
just as well.

Everything has been committed [MoxieDev][]. Now it's time to enjoy this
sunny day!

  [MoxieDev]: http://www.moxielogic.org/wiki/index.php?title=MoxieDev
