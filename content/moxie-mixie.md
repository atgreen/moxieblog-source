Title: Moxie Mixie: Frustrating Remote Attackers with Container Specific Instruction Sets
Date: 2016-01-14
Author: green
Category: moxie
Tags: gcc
Slug: moxie-mixie

While there are many existing technologies to frustrate remote
attackers, it can be fun to think up novel protections that might be
used to layer on additional defences.

Consider, for instance, that remote code execution through attacks
like buffer overflows depends on knowledge of the remote systems'
instruction set.  Knowledge of this instruction set allows attackers to
carefully construct payloads designed to take over your systems
through buffer overflow attacks and the like.  But what if we were
able to remove knowledge of the remote system ISA by essentially
making it unguessable?  Ladies and gentlemen, let me present to you
the Moxie Mixie architecture...

Mixie is a variant of the Moxie that uses the same instruction set as
Moxie, but with random instruction encodings, making it difficult for
remote attackers to generate payloads for execution.  Here's how it
works. Consider this C source code:

    int mycode (int a, int b)
    {
      return a + b;
    }

Here's what it would assemble to normally with the moxie GNU tools:

    00000000 <mycode>:
       0:    05 23          add     $r0, $r1
       2:    04 00          ret

To compile for the mixie variant, we need to assemble with the -mixie
option, and provide a random 128-bit key through the `MOXIE_MIXIE_KEY`
environment variable. So, for instance....

    $ MOXIE_MIXIE_KEY=123456789ABCDEF0 moxie-linux-as -mixie mycode.S

...produces...

    00000000 <mycode>:
       0:    05 23 77 5f    add     $r0, $r1
       4:    c6 1b
       6:    04 00 c9 23    ret
       a:    43 39

Note that each instruction now has an extra 32-bit suffix that is
randomly generated off of `MOXIE_MIXIE_KEY`.  We will always get those
same suffix values when we use the same key value.  If we change the
key...

    $ MOXIE_MIXIE_KEY=ABABABABABABABAB moxie-linux-as -mixie mycode.S

...we get different instruction encodings....

    00000000 <mycode>:
       0:    05 23 19 03    add     $r0, $r1
       4:    02 46
       6:    04 00 52 f1    ret
       a:    37 88
	    
Now on the other side of this, we need to execute the code in a
mixie-aware virtual machine.  This can be any simulator environment,
but QEMU in user mode is an interesting one.  In this mode, QEMU will
emulate the moxie mixie processor on Linux, but system calls are
passed through to the host (x86) platform.  Simply supply the same key
to the simulator and instructions will be recognized and executed as
expected.  Supply the wrong key, and all you'll get are illegal
instructions.  The take away here is that remote attackers, without
knowledge of the key, will have a difficult time generating a payload
to initiate their attack.

Run-time generated code presents a challenge that is easily
surmounted.  For example, GCC trampolines and libffi both generate
code at runtime and must have some way to generate instruction
encodings based on the appropriate mixie key.  In these cases, instead
of generating the code directly, we can generate a code generator that
asks the runtime (simulated mixie processor) to generate the code for
us.

Note that we're not 'encrypting' the binaries.  An attacker with
access to mixie binaries will trivially be able to map out the
instruction suffixes and generate shell code.  All we're doing here is
adding additional protections against remote attacks, where you have a
reasonable chance to secure physical access to the binaries.  We also
can't protect against DoS attacks using this technology.  If a remote
attacker can insert instructions into the target system, illegal
instruction crashes are certain to occur.

There are many interesting use cases, from embedded devices to
traditional web services.  Linux container technology, when combined
with QEMU, provide the perfect mixie platform that can deployed
anywhere regular docker containers can run.  All you need is a moxie
mixie linux userland and QEMU.

I'm interested in hearing feedack on this idea.  Thanks for reading!
