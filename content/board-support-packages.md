Title: Board Support Packages
Date: 2009-03-17 14:51
Author: green
Category: moxie
Tags: bsp, gdb, qemu
Slug: board-support-packages

Today we're introducing the notion of Board Support Packages (BSPs) to
the [moxie toolchain][].

A BSP provides all of the configuration data and code requires to target
a specific hardware platform. This mostly involves linker scripts,
platform initialization code, and hardware abstraction support
libraries.

Until recently the gdb sim was our only target platform. Now we also
have qemu, which needs to use [an alternate _write implementation][1]
in order to send output to a memory mapped UART. What we really need to
do is to define a "qemu" BSP that targets the default "board" defined in
qemu. This BSP will provide a support library with the UART version of
`_write`, and the original gdb sim version will live in a "sim" BSP.

In the world of the GNU toolchain, BSPs live in [libgloss][]. The
libgloss tree now contains BSP specific linker scripts which you must
use in order to pull in either of the BSP support libraries needed by
newlib. So if you want to target qemu, you run...

`$ moxie-elf-gcc -o hello.x hello.c -Tqemu.ld`

..and if you want to target the gdb sim, you have to go...

`$ moxie-elf-gcc -o hello.x hello.c -Tsim.ld`

This will make more sense down the line as we add more target boards
with different memory maps and peripherals.

Speaking of peripherals.... I've also added a Real Time Clock device to
the qemu board definition which I'll talk about in my next posting.

  [moxie toolchain]: http://moxielogic.org/wiki/index.php?title=Toolchain
  [1]: http://moxielogic.org/blog/?p=23
  [libgloss]: http://spindazzle.org/greenblog/index.php?/archives/106-ggx-libgloss,-newlib-and-hello.c.html
