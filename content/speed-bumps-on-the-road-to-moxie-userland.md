Title: Speed bumps on the road to moxie userland
Date: 2009-07-30 13:46
Author: green
Category: moxie
Tags: architecture, gcc, linux
Slug: speed-bumps-on-the-road-to-moxie-userland

Sooo..... it turns out there's lots to take care of before userland apps
like BusyBox can run.

-   **The root filesystem**. This one is easy. I just built a short
    Hello World application in C with moxie-uclinux-gcc. This produces
    an executable in [BFLT format][] which I call 'init'. The kernel
    build machinery takes this and produces a compressed root filesystem
    image linked to the vmlinux binary. The good news is that the kernel
    is able to boot, detect this [initramfs][], decompress it and load
    the init executable (which involves fixing up all of init's
    relocations). My Hello World doesn't actually use the C library or
    any system calls. It just writes Hello through [direct communication
    with the simulator via our software interrupt (swi) instruction][1].
    I thought this would let me avoid dealing with system calls for now.
    I was wrong...
-   **System calls**. This one is harder. Obviously (in retrospect!) the
    kernel creates the init process via the execve system call.
    Implementing system call support involves lots of platform dependent
    stuff. For instance, how do we invoke system calls? How are
    parameters passed? How do we switch back and forth between userland
    and the kernel? The first question is easy: I'll use our trusty
    [software interrupt (swi) instruction][] to invoke system calls.
    This means creating an exception handler and installing it as
    described [in this old post][].   
   As an aside, the swi instruction takes a 32-bit immediate operand.
    We currently use this to identify [calls to the simulator via
    libgloss][1]. This works well for escaping to the
    simulator, but isn't the best way to identify system calls to the
    kernel. The Linux kernel is going to ignore this operand, and we'll
    pass the system call ID in a register instead. This avoids us having
    to do complex instruction decoding in the exception handler
    processing the interrupt (also trashing any future data cache).
    Libgloss and the sim only need a small number of IDs, so I'm going
    to chop the swi instruction down from 48-bits to 16-bits in a future
    build of the tools.   
   Passing arguments to the system calls was also interesting to sort
    out...
-   **System call argument passing**. The moxie ABI currently only has
    two registers being used to hold function arguments. The remaining
    arguments must live on the stack. This decision goes back to when we
    only had 8 registers to play with. It turns out that Linux kernel
    system calls can have a maximum of 5 arguments. In order to avoid
    tricky argument marshaling, I've decided to try changing the general
    ABI accordingly, so that up to 5 registers may be used to hold
    function arguments. This involves changes to the compiler, debugger
    and a smattering of assembly language in libgloss.  
   The great thing about having integrated benchmarks into the
    [moxiedev][] environment is that you can easily compare before and
    after performance for ABI changes like this. Running "ant benchmark"
    runs through the [MiBench benchmark suite][] and saves a nice report
    for easy comparison. It turns out that switching from 2 to 5
    register arguments is almost universally a win in terms of both code
    size and instruction trace length (an approximation of run time).
    The consumer jpeg benchmarks were slightly larger and slower, but
    only by less than 1%. Every other benchmark result was slightly
    better. The one outlier was the "network\_dijkstra" benchmark which
    ended up 44% "faster" (44% fewer instructions being executed).
-   **The first real moxie compiler bug**. Sometimes things just don't
    work! This is especially true when you're tracking the bleeding edge
    from upstream. I won't go into the details, but I discovered a rare
    bug in the compiler where it would assume that compare results could
    live across function calls. Fortunately I was able to track down the
    guilty compilation pass and disable it with
    `-fno-rerun-cse-after-loop`. I know that some people have brought up
    kernels without the benefit of a nice debugger, but I just don't see
    how that is possible. The simulator, and a solid gdb port with
    reverse debugging capabilities have proven to be invaluable!

There's still lots to figure out and implement in the system call space,
but it's clear that we're getting very close to running our first Linux
program!

  [BFLT format]: http://www.beyondlogic.org/uClinux/bflt.htm
  [initramfs]: http://www.linuxfordevices.com/c/a/Linux-For-Devices-Articles/Introducing-initramfs-a-new-model-for-initial-RAM-disks/
  [1]: http://spindazzle.org/greenblog/index.php?/archives/107-ggx-Hello-World!.html
  [software interrupt (swi) instruction]: http://moxielogic.org/wiki/index.php?title=Instruction_Set#swi
  [in this old post]: http://moxielogic.org/blog/?p=148
  [moxiedev]: http://moxielogic.org/wiki/index.php?title=MoxieDev
  [MiBench benchmark suite]: http://www.eecs.umich.edu/mibench/
