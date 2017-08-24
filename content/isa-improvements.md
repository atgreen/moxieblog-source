Title: ISA improvements
Date: 2009-06-11 05:19
Author: green
Category: moxie
Tags: architecture
Slug: isa-improvements

I've committed the PC-relative branch instruction changes upstream. But
this is just one of many ISA improvements that need to happen. Here are
a handful of other ideas off the top of my head. None of these projects
should be particularly difficult.

-   Shorten load/store offsets to 16-bits. They are currently 32-bits,
    but for all of the benchmarks I've looked at the upper 16-bits are
    always 0x0000 or 0xffff. If the compiler ever really wants to use an
    offset > 16-bits, it should revert to computing the target address
    in registers. I don't expect that much code would require this.
-   Introduce shift instructions with immediate operands. There's plenty
    of opcode space for us to add 16-bit shift instructions that include
    a 5-bit immediate shift value (so we can shift up to 32-bits in
    either direction). Right now we load a 32-bit immediate shift value
    into a register which burns that register as well as wastes 32-bits
    of code space per shift.
-   Get the compiler to generate 16-bit immediate loads. All immediates
    are 32-bits right now, but the vast majority of these constants are
    < 16 bits long.
-   Push/pop multiple registers to the stack with one instruction.
    Although we have 16-registers, the ABI doesn't have us pushing all
    16 to the stack on function entry. We should be able to have a
    single 16-bit instruction that pushes/pops all of the relevant
    registers in one go. The instruction would include a bitmap
    identifying the registers we need to push/pop. ARM has something
    like this. The only drawback I can think of is that it could
    increase interrupt latencies as we'd probably have to retire the
    entire instruction (~10 memory writes/reads) before servicing an
    interrupt.
-   Many register rich ISAs include one register that is hardwired to
    zero. We could try this to see if it makes a difference, but I doubt
    it would be a win. Another idea would be to create a `cmpz`
    instruction to compare a register to zero so we don't have to burn a
    register for this common operation. Maybe cmp1 might even make
    sense. This is easy to measure.

Those are some of the obvious ones, and all I have time to write about
now.
