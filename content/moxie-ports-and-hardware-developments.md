Title: Moxie ports and hardware developments
Date: 2013-03-24 04:25
Author: green
Category: moxie
Tags: binutils, FreeRTOS, gcc, marin, MoxieLite, newlib, Nexys3, RTEMS
Slug: moxie-ports-and-hardware-developments

It's been a while since my last update.. let me bring you up to speed.

A couple of [libffi][] releases got in the way of moxie hacking
(although libffi 3.0.13 now includes full moxie support!), but things
are picking up speed again.

On the software side of things, the moxie [RTEMS][] and [QEMU][] ports
have both been accepted upstream. So now it's possible to build, run and
debug RTEMS applications on QEMU purely with upstream project sources.
You may notice that I'm doing much less work in the [moxiedev][]
repository these days. This was mostly just a staging area for moxie
software support (tools, OS), and there's little use for it now that
most everything is upstream. All of the moxie HDL work now happens in
the [moxie-cores][] git tree.

As for the hardware side of things, here are some of the recent changes:

-   The [MoxieLite][] core now supports [`ssr`][1] and [`gsr`][2]
    instructions, along with a bank of 16 special registers. The special
    register uses are defined here:
    <http://moxielogic.org/wiki/index.php/Architecture>
-   And now that the special register support is in place, exceptions
    and the [`swi`][3] (software interrupt) instruction are working in
    hardware. Semantics are defined here:
    <a href-"http: moxielogic.org wiki index.php exceptions" title="Exceptions" target="_blank">http://moxielogic.org/wiki/index.php/Exceptions</a>
-   `bad` (illegal) instructions now cause an illegal instruction
    exception
-   A simple interrupt controller has been added to the [marin][] SoC. I
    have the Nexys3 momentary switches hooked up as interrupt sources,
    so I can trigger interrupts and handle them in software by pressing
    those buttons.
-   A trivial timer has been hooked up to the interrupt controller, so I
    can now generate 'tick' interrupts for RTEMS in support of
    preemptive multitasking (everything was cooperative up 'til now).

I'm actually just debugging the timer ticks right now, but it's very
close.

And on a final note... while RTEMS is a great little embedded RTOS, it's
clear from this EE Times embedded survey that I'm going to have to
implement FreeRTOS support next:
<http://www.eetimes.com/electronics-news/4407897/Android--FreeRTOS-top-EE-Times--2013-embedded-survey>.
I think that's what I'll tackle after I get RTEMS running preemptively.

  [libffi]: http://sourceware.org/libffi "libffi"
  [RTEMS]: http://www.rtems.org "RTEMS"
  [QEMU]: http://www.qemu.org "QEMU"
  [moxiedev]: https://github.com/atgreen/moxiedev "moxiedev"
  [moxie-cores]: https://github.com/atgreen/moxie-cores "moxie-cores"
  [MoxieLite]: https://github.com/atgreen/moxie-cores/tree/master/cores/MoxieLite
    "MoxieLite"
  [1]: http://moxielogic.org/wiki/index.php/Instruction_Set#ssr
    "ssr"
  [2]: http://moxielogic.org/wiki/index.php/Instruction_Set#gsr
    "gsr"
  [3]: http://moxielogic.org/wiki/index.php/Instruction_Set#swi
    "swi"
  [marin]: https://github.com/atgreen/moxie-cores/tree/master/soc/marin
    "marin"
