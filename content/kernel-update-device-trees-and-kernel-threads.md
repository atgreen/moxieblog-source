Title: Kernel update: device trees and kernel threads
Date: 2009-07-25 04:50
Author: green
Category: moxie
Tags: gdb, linux, qemu
Slug: kernel-update-device-trees-and-kernel-threads

I've spent a lot of time in airports/planes/hotels recently, which is
good news for the moxie linux port. It runs about 6.5M instructions,
booting up to the point where a couple of kernel threads are created.
However, a few context switches later it all comes tumbling down. I
didn't have any of my kernel books with me, so I stopped hacking at that
point rather than try to guess/decode how some of the internals are
supposed to work.

My port is using a device tree to describe the system architecture. This
makes it easier to build a single kernel image that can boot on multiple
moxie implementations. There's a good paper on this relatively new
infrastructure here:
<http://ols.fedoraproject.org/OLS/Reprints-2008/likely2-reprint.pdf>. If
you've been following this project, you may recall that console I/O is
implemented differently on the gdb and qemu simulators. For the gdb
simulator we use a software interrupt instruction (swi) to [escape to
the simulator][], but the qemu port uses a real [simulated serial
device][]. This means they need different console devices in the kernel
to print boot messages. The device tree is a nice way to describe
differences like this and have a single kernel image to boot in both
environments.

Also, as predicted, I actually used moxie gdb's [reverse debugging][]
feature to help debug my kernel bring-up. It was *really* useful a
couple of times and has probably saved me the amount of effort required
to implement it in the first place already!

The next week is going to be very busy for me, so I don't expect to get
much done. We'll see...

  [escape to the simulator]: http://spindazzle.org/greenblog/index.php?/archives/107-ggx-Hello-World!.html
  [simulated serial device]: http://moxielogic.org/blog/?p=23
  [reverse debugging]: http://moxielogic.org/blog/?p=290
