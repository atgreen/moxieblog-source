Title: GTKWave Tip #1
Date: 2011-10-04 10:34
Author: green
Category: moxie
Tags: gtkwave, lisp
Slug: gtkwave-tip-1

GTKWave is a new tool for me, so I'll use this space to post useful tips
as I discover them.

The first tip comes from Tony Bybell, author of [GTKWave][], who pointed
me at some helpful functionality in a recent [blog comment][]. You can
enhance GTKWave's waveform display by replacing the normal data
presentation with something of your own design. So, for instance,
instead of looking at an opcode of "8033", you can see the disassenbled
moxie instruction `inc $fp 3`. You do this by implementing a program
that reads raw values from stdin and writes translations to stdout, and
then attaching this program as a filter to one of your signals.

I wrote a quick moxie disassembler in lisp ([gtkwave-opcodes.lisp][]),
and it is proving to be very handy!

<center>
[![gtkwave with moxie disassembly][1]](http://moxielogic.org/images/Screenshot-GTKWave-dump.vcd_.png)
</center>

  [GTKWave]: http://gtkwave.sourceforge.net "GTKWave"
  [blog comment]: http://moxielogic.org/blog/?p=511 "blog comment"
  [gtkwave-opcodes.lisp]: https://github.com/atgreen/moxiedev/blob/master/moxie/soc/muskoka/gtkwave/gtkwave-opcodes.lisp
  [1]: http://moxielogic.org/images/Screenshot-GTKWave-dump.vcd_-300x117.png
