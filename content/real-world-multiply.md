Title: Multiplication in the Real World
Date: 2014-12-24 08:47
Author: green
Category: moxie
Tags: moxie, gcc, architecture
Slug: real-world-multiply

The bitcoin team has been exercising moxie in ways that it hasn't been
stressed before.  For example, they've been examining the code quality
for their crypto libraries like
[libsecp256k1](https://github.com/bitcoin/secp256k1), an elliptical
curve crypto library in C.  One of their first feedbacks here was that
moxie provides no native way to get a 64-bit result from a 32-bit
multiply.  One of the developers noted that...

> 1. ARM has umull which returns results into two registers
> 2. PowerPC has no double-width result multiply, but does have mullw and mulhw instructions to compute the low and high word respectively
> 3. MIPS's multiplication goes into special hi and lo registers, which can be loaded into general-purpose registers later

From an instruction count perspective, moxie's failing here was
painfully obvious. But how to go about addressing this?

The MIPS and ARM approaches require register pairs to hold results.
Moxie has two-operand instructions, and if I went this way the second
register would have to be inferred somehow (`$rA` and `$r[A+1]`?).  Or
maybe we could dedicate special registers for multiplication results?
Neither approach is very appealing.  I decided to go with the Power
approach (also used by NIOS2 and perhaps others), and introduce new
instructions (`mul.x` and `umul.x`) that multiply two 32-bit values
and delivers the upper 32 bits of a 64-bit result (signed and
unsigned).  The compiler change was pretty straight forward, and can
be seen here:
[https://gcc.gnu.org/ml/gcc-patches/2014-12/msg01850.html](https://gcc.gnu.org/ml/gcc-patches/2014-12/msg01850.html).

Note that the compiler only generates these instructions when provided
with `-mmul.x`, which is enabled by default for moxiebox-elf targets.

The end result is that key functions in the secp256k1 code halved in
length!  We'll continue looking at code quality and tweaking the
architecture when it makes sense.
