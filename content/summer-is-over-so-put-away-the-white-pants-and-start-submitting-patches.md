Title: Summer is over, so put away the white pants and start submitting patches!
Date: 2009-09-10 14:21
Author: green
Category: moxie
Tags: gcc, gdb, linux, qemu, verilog
Slug: summer-is-over-so-put-away-the-white-pants-and-start-submitting-patches

It's been a while since my last update. What can I say... summer was
nice.

But now, back to business! I've just committed some long overdue patches
to the upstream GNU tools:

-   [Add a device tree blob to the gdb simulator][]. This lets us
    describe the gdb sim target to our single kernel image as described
    in [this posting][].
-   A GCC size optimization. Load 0 into a register [via xor][].
-   Improve function prologue [code generation][], and a corresponding
    [gdb change][].
-   [Use 6 registers to pass function arguments][] as [described
    here][].

This gets us to booting the kernel, loading BusyBox, running some shell
code and... crashing on the first fork. No problemo. Nothing a small
matter of programming can't fix. However, there are some other
distractions...

Verilog is lots of fun! It looks like regular programming, but it feels
more like building a kinetic sculpture.

There's also the small matter of not having an interrupt controller! So
there's some work here to design an interrupt controller, implement it
in verilog, simulate it qemu (and possibly the gdb sim), and port the
kernel over to using it. This should be interesting...

  [Add a device tree blob to the gdb simulator]: http://sourceware.org/ml/gdb-patches/2009-09/msg00289.html
  [this posting]: http://moxielogic.org/blog/?p=310
  [via xor]: http://gcc.gnu.org/ml/gcc-patches/2009-09/msg00651.html
  [code generation]: http://gcc.gnu.org/ml/gcc-patches/2009-09/msg00652.html
  [gdb change]: http://sourceware.org/ml/gdb-patches/2009-09/msg00287.html
  [Use 6 registers to pass function arguments]: http://gcc.gnu.org/ml/gcc-patches/2009-09/msg00653.html
  [described here]: http://moxielogic.org/blog/?p=395
