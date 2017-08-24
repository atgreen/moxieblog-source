Title: First moxie-linux userland app runs!
Date: 2009-08-17 20:11
Author: green
Category: moxie
Tags: linux
Slug: first-moxie-linux-userland-app-runs

I've been taking advantage of the nice summer weather recently, so it's
taken me a while to get around to this... but here's the first moxie
userland app!

    #include <string.h>

    #define MSG "Hello, World!\n"

    void __attribute__((noinline)) gloss_write (int fd, char *ptr, int len) 
    {
      asm("swi 5"); // "write" via the gdb simulator
    }

    int main()
    {
      while (1)
        gloss_write (0, MSG, strlen(MSG));
      return 0;
    }

If you build this with moxie-uclinux-gcc, name it `init` and
point the linux kernel build machinery at it, you'll get a kernel that
boots, loads the `init` BFLT binary from a ramfs, and performs an
`execve` system call on it! The program loops forever, printing "Hello,
World!" via the gdb simulator IO interrupt because I haven't fixed up
uClibc to perform system calls yet. Baby steps, my friends! Baby steps!
We will get there!

The main bit of work needed to get this going was to fix up the software
interrupt handler for system calls. I'm saving registers in a `pt_regs`
struct just prior to calling the `execve` system call. `execve` then
manipulates these saved registers so we end up running the newly exec'd
program when we "return" from the system call. This was all done in
[linux-2.6/arch/moxie/kernel/exception\_handler.S][1], which you can see
[here][1].

Next, I'll get uClibc to make system calls into the kernel so we can try
the same program with libc.a's `puts()`.

  [1]: http://github.com/atgreen/moxiedev/blob/4b1f3184f4a73347008c845d25e3f968f2afc569/linux-2.6/arch/moxie/kernel/exception_handler.S
