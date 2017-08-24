Title: It's Alive!
Date: 2012-09-14 14:39
Author: green
Category: moxie
Tags: architecture, fpga, gcc, gdb, Nexys3, SoC, VHDL, Xilinx
Slug: its-alive

There's a working hardware implementation of moxie in the wild!

Intrepid hacker [Brad Robinson][] created this moxie-compatible core as
a peripheral controller for his SoC. He had been using a simple 8-bit
core, but needed to address more memory than was possible with the 8-bit
part. Moxie is a nice alternative because it has a compact instruction
encoding, a supported GNU toolchain and a full 32-bit address space.
FPGA space was a real concern, so he started with a non-pipelined VHDL
implementation, and by all accounts it is running code and flashing LEDs
on a [Nexys3 board][]!

The one major "ask" was that there be a little-endian moxie architecture
and toolchain in addition to the default big-endian design. I had
somewhat arbitrarily selected big-endian for moxie, noting that this is
the natural byte order for TCP. In Brad's design, however, the moxie
core will handling FAT filesystem duties, which is largely a
little-endian task. At low clock speeds every cycle counts, so I agreed
to produce a bi-endian toolchain and, for the most part, it's all
committed in the upstream FSF repositories (with the exception of gdb
and the simulator). `moxie-elf-gcc` is big-endian by default, but
compile with `-mel` and you'll end up with little-endian binaries.

Brad also suggested several other useful tweaks to the architecture,
including changing the PC-relative offsets encodings for branches. They
had originally been encoded relative to the start of the branch
instruction. Brad noted, however, that changing them to be relative to
the end of the branch instruction saved an adder in his design. I made
this change throughout the toolchain and (\*cough\*) documentation.

I'll write more about this as it develops... Have to run now.

Oh. Here's the VHDL on github:
<http://github.com/toptensoftware/MoxieLite>. Go Brad!

AG

  [Brad Robinson]: https://twitter.com/toptensoftware "Brad Robinson"
  [Nexys3 board]: http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,400,897&Prod=NEXYS3
    "Nexys3"
