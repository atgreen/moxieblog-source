Title: vfork() for uClinux forces an architecture change
Date: 2012-09-03 07:35
Author: green
Category: moxie
Tags: architecture, linux
Slug: vfork-for-uclinux-forces-an-architecture-change

Moxie uses a simple software interrupt instruction (`swi`) to implement
system calls. The `swi` instruction creates a call frame on the stack
and then jumps to a global exception handler routine. The exception
handler for moxie-uClinux switches to the kernel stack before jumping to
the relevant kernel routine. Returning from an exception becomes a
simple `ret` instruction because we have a nice call frame on our stack.
Very simple.

`vfork()`, a kludge that was ejected from posix, but is still required
for MMU-less uClinux ports, throws this for a loop. The `vfork` system
call creates a child process that shares memory with the parent,
including a shared stack. This means that the `vfork` system call
*returns twice on the shared stack*: once for the child, and then again
for the parent. The problem is that the child, once returned, is going
to write over the `swi` call frame on the shared stack as it continues
to do work. This sends the parent off into randomland when it eventually
returns using the corrupted call frame.

Actually, it's not just the `swi` call frame. There's also the `vfork()`
stack frame from the C library to worry about.

This problem isn't unique to moxie. If you examine the x86 uClibc
`vfork()` implementation, you'll see that it stashes all the info it
needs for the return in registers that are preserved over the `vfork`
system call.

For moxie, I'll likely need to do the same thing in uClibc's `vfork()`,
but I'm also going to change the semantics of the `swi` instruction.
This means formalizing the notion of user mode and kernel mode. The
uClinux port already does this by convention. One of the special
registers is used to store the Linux kernel-mode stack pointer. The
`swi` instruction will be changed to immediately switch stacks and push
the userland return info onto the non-shared kernel stack, leaving the
shared user stack completely untouched. The exception handler will have
a bit more house keeping to do, but `vfork()` should work.
