Title: Native On-Chip GDB Remote Protocol Support
Date: 2012-11-24 05:47
Author: green
Category: moxie
Tags: gdb, JTAG, marin, SoC
Slug: native-on-chip-gdb-remote-protocol-support

A typical software debug solution for an embedded systems might involve
a [JTAG][] connection to the board, and then some kind of protocol
translation software that handles communication between GDB's remote
serial protocol and the target JTAG port (see [OpenOCD][], for
instance). The FPGA systems I'm working with include JTAG ports, and the
vendors also provide JTAG IP cores for interfacing them to your digital
logic. On the other hand, these systems also have nice UARTs that are
easy to talk to. We have the opportunity to dramatically simplify the
debug toolchain by including support for GDB's remote protocol directly
on chip. This would be a hardware implementation of the protocol - no
software stubs required.

The GDB Target Engine IP core is essentially a state machine that reads
GDB packets coming over the UART (a microusb connection to my laptop).
It has direct access to MoxieLite core through some additional wires for
extracting register values. It also acts as a bus master to read/write
directly to/from memory. The Marin SoC only has one bus master - the
moxie core. The nice thing here is that we don't have to add any new bus
arbitration logic for the second master, because only one master will
ever be active at a time. We're either running in debug mode (active
connection to GDB over the UART), in which case the GDB Target Engine is
the bus master, or we're running in regular mode, where the moxie core
is in control.

The GDB remote protocol includes many commands these days, but only a
small number are required to be supported by the target: read/write
registers, read/write memory, step and continue.

Current status is that I can connect GDB directly to the SoC using
"target remote /dev/ttyUSB0", at which point GDB negotiates with the
target to determine what features are supported. I can hit Ctrl-C in GDB
to tell the SoC to enter debug mode. The Target Engine core then talks
to MoxieLite to extract register values, converts them to ASCII text and
sends them back to the debugger over the wire. This includes the PC, so
GDB knows where to go. Given that this is working, I'm not too worried
about the rest of it - but only time will tell...

  [JTAG]: http://en.wikipedia.org/wiki/Joint_Test_Action_Group
  [OpenOCD]: http://openocd.sourceforge.net/
