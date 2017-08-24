Title: Multiported Registers, Microcode and Register Forwarding
Date: 2012-07-01 14:46
Author: green
Category: moxie
Tags: muskoka, verilog
Slug: multiported-registers-microcode-and-register-forwarding

When I last wrote about tackling the 'pop' instruction I noted that I
needed the ability to write to multiple registers before retiring that
one instruction - something that would require extra instruction cycles
or loads more logic. I recently came across some work by Charles Eric
LaForest on [Efficient Multi-Ported Memories for FPGAs][]. His Live
Value Table (LVT) approach solves my problem quite neatly, and I was
able to adapt some of his sample code for a new register file
implementation that supports 2 simultaneous writes as well as 4 reads.

One more recent change includes the addition of microcoded pipeline
control signals. I simply created a [text file managed with emacs
org-mode][] that describes pipeline control signals used for each
instruction. A little [lisp script][] reads this and turns it into a
binary table that is read during the instruction decode stage. Passing
the signals down the pipeline is much simpler than hand coding
behaviours in a big switch statement.

Also, quite some time ago I wrote about handling Read-After-Write
pipeline hazards by inserting bubbles into the pipeline. I replaced that
with some [register forwarding][] logic, so you can read a register
immediately after writing to it without introducing any delays.

So... progress is being made! I think I'll be running my first C program
soon.

  [Efficient Multi-Ported Memories for FPGAs]: http://www.eecg.utoronto.ca/~laforest/multiport/index.html
    "Efficient Multi-Ported Memories for FPGAs"
  [text file managed with emacs org-mode]: https://raw.github.com/atgreen/moxiedev/master/moxie/cores/moxie/microcode.org
    "text file managed with emacs org-mode"
  [lisp script]: https://github.com/atgreen/moxiedev/blob/master/scripts/microcoder.lisp
    "lisp script"
  [register forwarding]: http://en.wikipedia.org/wiki/Hazard_%28computer_architecture%29#Register_forwarding
    "register forwarding"
