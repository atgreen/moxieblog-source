Title: A Verilogical Place To Start *
Date: 2009-04-07 20:31
Author: green
Category: moxie
Tags: verilog
Slug: a-verilogical-place-to-start

I've written my first bit of [verilog][] tonight. It's not much, really,
but it's a start. I'm using [Icarus Verilog][] (iverlog) to compile and
simulate the code. I also plan on using [GTKWave][] to examine timing
dumps from the iverilog simulator. Both of these tools are part of my
development platform, Fedora.

Rather than plan everything out to the last detail, I'm going to wing it
for a while and explore the language. To start with, I've decided to try
to hack the core together as a simple pipelined processor consisting of
the following four stages: Instruction Fetch, Instruction Decode,
Execute and Write.

The first complication comes from Moxie's long instructions. Moxie is
not RISC processor, in that it does not have fixed width instructions
that can be fetched in a single go. Most of the instructions are
16-bits, but several of them are 48-bits, the last 32-bits being some
kind of immediate value. We're going to have a 32-bit path to
instruction memory, which means we may have to fetch twice in order to
read a single instruction. This involves state machinery and some tricky
back and forth between the Instruction Fetch and Instruction Decode
pipeline stages. It's taking a while to get straight in my head, so I
don't know when my next update will be.

\* Blog entry title borrowed from [this great book][]

  [verilog]: http://en.wikipedia.org/wiki/Verilog
  [Icarus Verilog]: http://www.icarus.com/eda/verilog/
  [GTKWave]: http://www.gpleda.org/tools/gtkwave/index.html
  [this great book]: http://assets.cambridge.org/97805218/28666/excerpt/9780521828666_excerpt.pdf
