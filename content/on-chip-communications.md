Title: On-chip communications
Date: 2010-10-06 04:37
Author: green
Category: moxie
Tags: architecture, SoC, wishbone
Slug: on-chip-communications

I need to build real SoC infrastructure around my developing core in
order to test it on real hardware. For the most part, this means a
memory controller and IO devices. I've decided to implement a shared-bus
wishbone-style interconnect for these devices. [Wishbone][] is an open
source on chip bus architecture that is popular with many open core
developers. While not perfect, wishbone is a good choice for this first
SoC due its simplicity and the ample supply of sample implementations.

The main complaints about wishbone are the lack of efficient semaphore
operations (the bus remains locked for an entire read/modify/write
operation) and the lack of pipelined reads/writes. This doesn't bother
me for the moment. I just need a simple interconnect so I can focus on
debugging the moxie core part of the SoC.

By the way, there's a terrific book on this subject called "On-Chip
Communication Architectures". Chapters 2 and 3 are great introductions
to on-chip interconnects, and it looks like Google Books has the entire
chapter 2 online here...

<iframe frameborder="0" scrolling="no" style="border:0px" src="http://books.google.ca/books?id=uR3Vw9mYtpIC&amp;lpg=PP1&amp;ots=ZBpqbO_QDG&amp;dq=On-Chip%20Communication%20Architectures&amp;pg=PA145&amp;output=embed" width="500" height="500"></iframe>

  [Wishbone]: http://en.wikipedia.org/wiki/Wishbone_%28computer_bus%29
