Title: Putting it together: on-chip firmware
Date: 2013-12-10 03:45
Author: green
Category: moxie
Tags: gdb, marin, Nexys3, r
Slug: putting-it-together-on-chip-firmware

The on-chip [firmware][] for the [Marin SoC][] has been updated with the
gdb stub, so now when you program the FPGA, you'll see the following on
the serial console:

    MOXIE On-Chip Bootloader v2.0
    Copyright (c) 2013 Anthony Green 

    Waiting for an S-Record Download or Remote GDB Connection...

...and the Nexys3 7 segment display reads "FEEd". At this point you can
send down an srecord encoded binary that will then start running at
0x30000000 (7 segment display reads "3000"), or connect with
moxie-elf-gdb (7 segment display reads "dEb2"). A typical gdb session
looks like this:

<p>
<script src="https://gist.github.com/atgreen/7889219.js"></script>
</p>
The final bit of the puzzle was a missing feature in the on-chip RAM
controller -- not external RAM, but RAM cobbled together from FPGA logic
which is used by the on-chip firmware for stack & heap. I had left out
byte-level access in my initial design, so every read/write was 16-bits
- potentially wiping out memory unintentionally. Once I [figure this
out][], everything started to work.

I'm done with the on-chip bootloading firmware for now!

  [firmware]: https://github.com/atgreen/moxie-cores/blob/master/firmware/bootrom/tinystub.c
    "firmware"
  [Marin SoC]: https://github.com/atgreen/moxie-cores/tree/master/soc/marin
    "Marin SoC"
  [figure this out]: https://github.com/atgreen/moxie-cores/commit/4ec58e177d44d04532b3490e9a11df13d35fb63c
