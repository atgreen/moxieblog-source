Title: A Tiny Computer
Date: 2009-03-13 14:48
Author: green
Category: moxie
Tags: verilog
Slug: a-tiny-computer

[Lambda the Ultimate](http://lambda-the-ultimate.org/) today posted a interesting blog entry on [A Tiny
Computer](http://lambda-the-ultimate.org/node/3232). It refers to 2007 paper by Chuck Thacker at Microsoft
Research describing a tiny 32-bit processor. Appendix A of the paper
includes the entire synthesizeable verilog implementation in just a page
and a half of code! Here's a direct link to the PDF:
<http://www.bottomup.co.nz/mirror/Thacker-A_Tiny_Computer-3.pdf>.

I plan on using verilog for my initial moxie implementation. I'm told
that it's the clear choice from a tools perspective. There's even a free
software implementation already packaged for [Fedora](http://fedoraproject.org): [Icarus
Verilog](http://www.icarus.com/eda/verilog). As far as eduction is concerned, I've mainly been using the
two terrific books show below. Do you have any better suggestions? I'd
love to hear them.

Now, however, I'm still debugging GDB's interaction with qemu. It mostly
involves watching [remote protocol](http://sourceware.org/gdb/current/onlinedocs/gdb_34.html#SEC721) traffic, looking up the packet
codes, and then trying to understand why the simulator is not behaving
as expected. Good times...
