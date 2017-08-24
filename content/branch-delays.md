Title: Branch delays
Date: 2011-09-28 07:13
Author: green
Category: moxie
Tags: architecture, gas, verilog
Slug: branch-delays

I've coded up logic for more arithmetic instructions, register moves, as
well as direct and indirect jumps. For jumps, I simply pass a branch
signal from the execute stage back to the fetch stage, as well as the
computed target address. Here's some code that works now:

    .text
        xor $r0, $r0 # Zero out $r0
        mov $r1, $r0
        mov $r2, $r0
        mov $r3, $r0
        mov $r4, $r0
    loop:   inc $r0, 0x1 # Increment $r0
        inc $r1, 0x1
        inc $r2, 0x1
        inc $r3, 0x1 
        inc $r4, 0x1 
        jmpa    loop+0x1000 # Offset hack
        nop
        nop

A couple of things to note... Boot ROM is mapped into the address space
at 0x1000, which explains the offset hack above. A linker script is
probably the right way to do this. Using ".org 0x1000" at the start of
the source appears to pad the resulting object with 0x1000 bytes of
nothing, which means it doesn't fit into the small space I've allocated
for bootrom.

Also note that I've got to deal with branch delay slots. I'm not exactly
sure what I want to do yet. Due to the nature of the variable width
instruction encoding, it looks like you can have either 1 or 2 delay
slots to fill, depending on the instruction sizes. I don't like this at
all. I'll probably end up limiting it to one delay slot.

This is one of those ugly areas where implementation informs design. I'd
rather not have delay slots at all, but it's hard to ignore the
performance gain.
