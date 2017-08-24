Title: Fetching instructions
Date: 2010-09-07 13:56
Author: green
Category: moxie
Tags: architecture, verilog
Slug: fetching-instructions

Moxie requires some interesting instruction fetch logic.

For my initial implementation I'm assuming a 32-bit path to instruction
memory. But moxie has both 16- and 48-bit instructions, so it's not like
simple RISC cores that can feed the pipeline on every cycle. My solution
is to feed 32-bit instruction memory words into a Instruction FIFO. 16-
and 48-bit instructions pop out of the other end of the FIFO on every
cycle (or a NOP bubble when we're waiting for the last 16 bits of a
48-bit instruction). My initial Instruction FIFO is 64-bits long. From
my simple testing it looks like this does a reasonable job of keeping
the instruction memory path busy, and issuing instructions as often as
possible (I'm just eyeballing the gtkwave output, reproduced below). I
can experiment with a longer Instruction FIFO later.

![][]

This image shows a few signals from the Instruction FIFO. valid\_o tells
us that we're popping off a valid instruction from the FIFO, whereas
full\_o tells us not to write any data to the FIFO because it's full. So
far, so good - decoupling the fetching of instruction memory from the
rest of the pipeline is obviously the right thing to do.

One more complication that I'm going to punt on for now is PC tracking.
Eventually we'll want to pass the PC down the pipeline so we get
accurate exception addresses. Tracking the PC through the Instruction
FIFO is just one more little complication that I'll tackle after I make
more progress on the rest of the microarchitecture.

I've only done some behavioral simulation so far, but I believe the code
is synthesizable. The code is in github here: <http://bit.ly/9yVQ7U>.
Running make should build everything, then just run "a.out".

Note that I'm using magic instruction memory: an array populated with a
hello world app built like so...  

`$ moxie-elf-gcc -o hello.x -O2 hello.c -Tsim.ld $ moxie-elf-objcopy -O verilog hello.x hello.vh`  
And the verilog simulator reads hello.vh directly. Pretty cool!

(I just realized I wrote about fetching instructions [almost 18 months
ago][] - that took too long!)

  []: http://moxielogic.org/blog/wp-content/uploads/2010/09/fetch.png
    "waves from the moxie Instruction FIFO "
  [almost 18 months ago]: http://moxielogic.org/blog/?p=161
