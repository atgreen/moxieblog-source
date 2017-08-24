Title: Thinking about exceptions....
Date: 2009-03-19 14:01
Author: green
Category: moxie
Slug: thinking-about-exceptions

In reading about how other processors handle exceptions, they seem to be
of two sorts. Some (most?) processors look into a vector of exception
handlers based on the exception type (Divide by Zero, Software
Interrupt, IRQ, etc), and the other sort jumps to a single exception
address and lets the software sort it out. I'm thinking of going this
second route, only because it seems simpler and more flexible. The
address of the handler will live in one of the special registers, and
will need to be initialized with a [Set Special Register][] (`ssr`)
instruction. Next we need to decide on what calling convention to use to
get to the handler. Is there any reason not to use the standard calling
convention? It certainly will make things easier for the debugger and I
maybe I can reuse the stack slot reserved for the static chain pointer
to hold the exception type. Many processors, however, just load the
return address into a reserved register and jump to the handler.
Presumably this is for performance reasons. More thought required... but
feedback welcome!

  [Set Special Register]: http://spindazzle.org/greenblog/index.php?/archives/120-ggx-new-instructions-and-porting-the-Linux-kernel.html
