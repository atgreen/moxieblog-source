Title: Reverse debugging!
Date: 2009-07-12 21:55
Author: green
Category: moxie
Tags: gdb
Slug: reverse-debugging

A few weeks ago I happened to be in Palo Alto and met up with my friend
and long-time GDB hacker Michael Snyder. He told me about a new feature
in GDB called "process recording". The basic idea is that when you tell
GDB to enter into "record mode", it records undo information for every
instruction executed during the debug process. This lets you switch
direction and start stepping through your code backwards in time! It's a
pretty amazing feature.

I was anxious to implement it for moxie, but only got around to it this
weekend. The [moxie ISA][] is relatively small, so it wasn't much work.
The patch looks something like [this][]. And, as promised, you can now
step forwards and backwards through moxie code. Reverse "continue" and
"finish" also work. It's going to be really handy when I get back to
working the Linux kernel port.

Some GDB front-ends already have the controls in place for reverse
debugging. Here's a webinar [showing reverse debugging on Eclipse][]. I
mostly use Emacs as my moxie-elf-gdb frontend, but I'm not sure if it
supports the reverse instructions nicely yet (of course you can "set
exec-direction reverse" and use the normal step/next/continue commands).

Thanks to Micheal for pointing me at this new feature, and to Tea Water
for implementing process recording in the first place.

**UPDATE:**Emacs support for reverse debugging [should be arriving in
23.2][]. I'm not sure what the schedule for that is, but 23.1 is
supposed to come out next week (July 22).

  [moxie ISA]: http://www.moxielogic.org/wiki/index.php?title=Instruction_Set
  [this]: http://github.com/atgreen/moxiedev/commit/e8940639760db3ae05f01ef205d93d85fb3f4ab1
  [showing reverse debugging on Eclipse]: http://live.eclipse.org/node/723
  [should be arriving in 23.2]: http://sourceware.org/ml/gdb/2009-07/msg00094.html
