Title: Progress...
Date: 2009-03-12 20:34
Author: green
Category: moxie
Tags: gcc, qemu, releng
Slug: progress

I made some progress on using moxie-elf-gdb with qemu the other day.
Qemu has an integrated gdb stub, so GDB speaks to it via the remote
protocol. It's still not quite there, but getting close. I'm anxious to
get it working, as it's the last step before hacking on the Linux kernel
port.

I've also tweaked the "ant srpm" target, so it creates clean SRPMs for
binutils, newlib, gcc, gdb and qemu. Well, sort of. When building GCC
from scratch you actually have to build it twice: once to build newlib,
and the second time with the installed newlib. This is easy enough to
handle in MoxieDev where I have a single tree and full control over the
build sequence. It's a little bit weirder in RPM-land because of the
circular dependencies between packages. I was able to bootstrap it on my
system, but it's a hack. I may resort to merging the newlib sources into
the GCC SPRM, and then make newlib a subpackage of gcc. Release
engineering is the suck!

And, finally, I've merged the latest and greatest trunk revisions of gcc
and src into MoxieDev. Woooo - it all still works! Check out the commit
logs in the [blog sidebar][].

  [blog sidebar]: http://moxielogic.org/blog
