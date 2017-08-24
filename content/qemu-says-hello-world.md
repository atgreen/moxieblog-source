Title: Qemu says Hello, World!
Date: 2009-03-07 06:22
Author: green
Category: moxie
Tags: qemu
Slug: qemu-says-hello-world

Virtually all of the simulation done so far was with the GDB instruction
set simulator. As a basic instruction set simulator, it was limited to
executing instructions found in typical "user level" applications. And,
if you recall, all interaction with the outside world happened through
magic software interrupts that were intercepted by the simulator. I
wrote about this interaction way back here:
<http://spindazzle.org/greenblog/index.php?/archives/107-ggx-Hello-World!.html>.

Instruction set simulators are interesting for one reason: they're easy
to write! It's simple to whip up a sim in the early stages of toolchain
development in order to test your tools. In fact, almost every GCC port
has a corresponding instruction set simulator to test the compiler's
output. On the other hand, the basic instruction set simulator is not
capable of running more interesting software, like operating system
kernels, because they don't simulate any of the ancillary features of a
microprocessor: peripherals, timers, interrupt controllers, MMUs, etc.
This is where system simulators come into play.

For the moxie toolchain, I've selected the popular [qemu](http://qemu.org) simulator.
Several months ago I wrote about my start with qemu here:
<http://spindazzle.org/greenblog/index.php?/archives/123-qemu-ggx-softmmu-starts-crawling.html>.
Well, a lot of that work had to be rewritten for the new qemu (version
0.10 was just released last week). Qemu switched from a simple template
compiler to using a real C compiler backend from the [Tiny C Compiler](http://bellard.org/tcc)
project. The template compiler (dyngen) stitched together fragments of
pre-compiled code at runtime, while the new TCG backend is a proper x86
compiler with simple optimization passes.

In practice, this wasn't a huge amount of work. The translator still
looks like a huge switch statement where we handle each opcode. For
instance, here's a register-to-register move:

     case 0x02:  /* mov (register-to-register) */
       {
         int dest = (opcode >> 4) & 0xf;
         int src = opcode & 0xf;
         tcg_gen_mov_i32(REG(dest), REG(src));
       }

`tcg_gen_mov_i32` generates the intermediate code to move the value
between registers.

Once I had implemented support for enough instructions, I was able to
run a trivial Hello World program straight through:  

    $ cat hello.c
    #include <stdio.h>

    int main()
    {
      puts ("Hello World!");
      return 0;
    }
    $ moxie-elf-gcc -o hello.x hello.c
    $ qemu-system-moxie -nographic -kernel hello.x
    qemu: fatal: Trying to execute code outside RAM or ROM at 0x00000000

    pc=0x00000000
    $fp=0x00000000 $sp=0x0000000c $r0=0x00000001 $r1=0x000055c4
    $r2=0x00000000 $r3=0x00000000 $r4=0x001ffff4 $r5=0x00000000
    $r6=0x00000000 $r7=0x00000000 $r8=0x00000000 $r9=0x00000000
    $r10=0x00000000 $r11=0x00000000 $r12=0x00000000 $r13=0xfffffff4
    Aborted

Oops. Two problems: no "Hello, World" output and the fatal error. The
fatal error is simple to explain. The moxie qemu port defines a virtual
hardware platform, with physical memory mapped way up at 0x8000000.
Somehow the simulator is trying to execute code outside of our physical
memory range. The reason turns out to be simple. Unlike our simple
instruction set simulator, system simulators like qemu don't expect to
run programs that "exit". They're designed to run operating systems that
start running and never finish. If you look carefully above you'll see
that I'm asking qemu to run a "kernel" called hello.x. Well, hello.x is
actually just a regular user program that exits. In this case, the
processor is running off of the end of the \_\_init entry point and
pulling an uninitialized return address off of the stack, sending us off
to execute code at 0x00000000.

But where is "Hello, World"? We're still linking in libgloss, which is
trying to "\_write" output with our special software interrupt. That's
not going to work here. We don't want to implement magic IO in a system
simulator. We want to simulate real IO! One of the beautiful things
about qemu is that it comes with a wealth of simulated peripherals that
you can hook up to your processor. So, for now, let's just send all
output to a simulated serial port. Qemu makes this very simple. In the
module that defines our hardware platform, we just add:  

        /* A single 16450 sits at offset 0x3f8.  */
        if (serial_hds[0])
          serial_mm_init(0x3f8, 0, env->irq[4], 8000000/16, serial_hds[0], 1);

Now we just have to override the \_write in libgloss to write to the
16450 UART which has been mapped to memory at 0x3f8. Qemu's default
setting has all serial port output going to the console. So now....

    $ cat hello.c
    #include <stdio.h>

    int _write (int fd, char *buf, int len)
    {
      int i = 0;
      while (i < len)
        *(char *)0x3f8 = buf[i++];
      return len;
    }

    int main()
    {
      puts ("Hello World!");
      return 0;
    }
    $ moxie-elf-gcc -o hello.x hello.c
    $ ./qemu-system-moxie -nographic -kernel hello.x
    Hello World!qemu: fatal: Trying to execute code outside RAM or ROM at 0x00000000

    pc=0x00000000
    $fp=0x00000000 $sp=0x0000000c $r0=0x00000001 $r1=0x000055c4
    $r2=0x00000000 $r3=0x00000000 $r4=0x001ffff4 $r5=0x00000000
    $r6=0x00000000 $r7=0x00000000 $r8=0x00000000 $r9=0x00000000
    $r10=0x00000000 $r11=0x00000000 $r12=0x00000000 $r13=0xfffffff4
    Aborted

Very nice!
