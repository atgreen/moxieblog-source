Title: Fake RAM, load/store and push
Date: 2011-10-11 19:00
Author: green
Category: moxie
Tags: muskoka, SoC, wishbone
Slug: fake-ram-loadstore-and-push

Progress report time....

I need RAM in order to implement/test most instructions. To that end,
I've implemented a fake data cache that is always accessed within a
single cycle during the WRITE pipeline stage. Eventually this will have
to be replaced with a real data cache that reads/writes to real memory
over the wishbone bus while the processor pipeline stalls.

The `push` instruction was easy enough to implement. It's the first one
that writes to both memory and a register (to update the stack pointer).
This meant reworking the interface between the EXECUTE and WRITE stages.
`pop` is a little more tricky because we need to update two registers:
the stack pointer and the register we're loading memory into. I'm going
to work this out tomorrow night, but I can see now how making it work in
a single cycle will require a little more logic than splitting it up
into two cycles. It will be interesting to experiment with changes like
that once everything is working.

Also, I reorganized the HDL source to cleanly separate the moxie core
from the muskoka SoC and related firmwares and cores. As usual,
everything is in [github][].

  [github]: http://github.com/atgreen/moxiedev "moxiedev"
