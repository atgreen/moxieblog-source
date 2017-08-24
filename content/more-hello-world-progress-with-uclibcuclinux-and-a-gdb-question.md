Title: More hello world progress with uClibc/uClinux, and a GDB question.
Date: 2009-08-18 21:49
Author: green
Category: moxie
Tags: gdb, linux
Slug: more-hello-world-progress-with-uclibcuclinux-and-a-gdb-question

Tonight I got a hello world app to use uClibc's `puts()` routine! This
is a big deal because it's the first time I've had system calls coming
in from userland. I haven't checked the changes in yet, because they're
a mess, but here's a basic run-down of what I had to do...

-   First, uClibc had to be taught how to make system calls to the moxie
    uClinux kernel. This was straight forward, except I came across one
    surprise which I'll describe below.
-   Next, I needed to add more files to my initfs. Specifically, I
    needed a /dev/console. Fortunately, the kernel build process makes
    this easy. I decided to use the "text file" approach to populating
    the initramfs as described in [this document][].
-   Finally, I had to create a tty device for my default console that
    spoke through the gdb simulator via software interrupts. Fortunately
    the ia64 port had a similar tty device for talking through one of
    HP's simulators that I was able to mostly copy.

Once all this was done, I was able to build a standard Hello World app
with moxie-uclinux-gcc, and it just worked!

What about the system call surprise? Despite what I read somewhere that
said that Linux system calls had a maximum of 5 parameters -- that's not
quite true. Some take 6 (are there any with 7? more?). This thwarted my
attempt to get busybox running tonight, because it uses mmap, and mmap
is one of those 6-argument system calls. There are a few ways to fix
this. I think I'll just hack the compiler to use 6 register arguments
and see what that does to code size/performance.

If there are any GDB hackers reading this... I have one question for
you... The kernel is loading and relocating my "init" program, then
execve'ing it. When I run the kernel in gdb, it would be nice for gdb to
load the debug info for init so I could see what it's doing when I step
into userland. Is there some way to do this manually?

  [this document]: http://www.kernel.org/doc/Documentation/filesystems/ramfs-rootfs-initramfs.txt
