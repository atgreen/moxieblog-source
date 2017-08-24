Title: Pipeline hazards
Date: 2010-09-10 13:25
Author: green
Category: moxie
Tags: architecture, verilog
Slug: pipeline-hazards

I've coded up a first go at four pipeline stages so far: [Fetch][],
[Decode][], [Execute][], and Write. After the relative complexity of the
[Fetch implementation][], the rest has been pretty straight forward, and
I've started running the first bit of compiled code through the pipline.
Here's that start of our Hello World C application. It's `__start` from
crt0.o:

    00001000 <__start>:
        1000:       01 10 00 40     ldi.l    $sp, 0x400000
        1004:       00 00
        1006:       01 00 00 00     ldi.l    $fp, 0x0
        100a:       00 00
        100c:       91 0c           dec      $sp, 0xc

This code simply initializes the stack and frame pointers, and makes
room for a new stack frame (just ignore the obvious inefficiencies for
now!).

Running this through the pipline, I can see the first `ldi.l` make it's
way through Fetch, Decode, Execute (basically nothing) and Write. The
second `ldi.l` works similarly. Then we get to the `dec`. In order to
decrement, we need to read the $sp from the register file in Decode,
perform the subtraction in Execute, and save it back to the register
file in Write. But when I first ran it through the [verilog simulator][]
I saw the `dec` instruction reading `0x00000000` from $sp instead of
`0x400000`. I'm only three instructions into my first simulation and
I've hit my first pipeline hazard! The `0x400000` from the first
instruction hasn't been written to $sp yet, as we're just about to
start the Write stage for that instruction!

So the next step is to add a little hazard detection to the pipeline
control logic. I'm going to stick with [pipeline interlocks][] for now
(stuffing NOPs in the middle of the pipeline) instead of more
complicated [forwarding logic][].

As usual, [everything is in moxiedev][]. Just "cd
moxiedev/moxie/rtl/verilog && make && ./a.out" to run the simulation.

  [Fetch]: http://github.com/atgreen/moxiedev/blob/master/moxie/rtl/verilog/cpu_fetch.v
  [Decode]: http://github.com/atgreen/moxiedev/blob/master/moxie/rtl/verilog/cpu_decode.v
  [Execute]: http://github.com/atgreen/moxiedev/blob/master/moxie/rtl/verilog/cpu_execute.v
  [Fetch implementation]: http://moxielogic.org/blog/?p=444
  [verilog simulator]: http://www.icarus.com/eda/verilog/
  [pipeline interlocks]: http://homepage3.nifty.com/alpha-1/computer/Interlock_E.html
  [forwarding logic]: http://en.wikipedia.org/wiki/Hazard_%28computer_architecture%29#Register_forwarding
  [everything is in moxiedev]: http://github.com/atgreen/moxiedev
