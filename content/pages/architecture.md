Title: Architecture
Date: 2014-12-29 01:15
Author: admin
Status: hidden
Slug: architecture

# Overview

Moxie is a general purpose bi-endian load-store processor, with
sixteen 32-bit general purpose registers and a comprehensive ISA.  It
was originally designed to be an ideal target for the [GNU Compiler
Collection](http://gcc.gnu.org), and has since evolved to include many
supervisory level instructions required to run an embedded RTOS such
has [RTEMS](http://rtems.org).

Most moxie instructions are 16-bits long, while the remainder include
an additional 16- or 32-bit immediate value resulting in 32- and
48-bit instructions.  A variable width instruction architecture was
chosen over a fixed-width RISC implementation in order to optimize for
instruction memory bandwidth, a key performance limiter for many FPGA
applications.

As a fair warning to readers, it should be mentioned that the moxie
architecture is still evolving.  That being said, there have been few
changes in recent history.  Feedback, of course, is certainly welcome!
Please send all comments to the
[author](http://moxielogic.org/blog/pages/author.html).

# Registers

Moxie defines 16 32-bit registers as follows:
<div class="fancy">
<center>
<table>
<tr><th>Name</th><th>Description</th></tr>
<tr><td>`$fp`</td><td>the frame pointer</td></tr>
<tr><td>`$sp`</td><td>the stack pointer</td></tr>
<tr><td>`$r0` through `$r13`</td><td>general purpose registers</td></tr>
</table>
</center>
</div>
In addition, there are a number of special registers whose values are accessible only with the Get Special Register (`gsr`) and Set Special Registers (`ssr`) instructions.   Some of these registers have special purposes:

<div class="fancy">
<center>
<table>
<tr><th>Special Register</th><th>Description</th></tr>
<tr><td>0</td><td>status register with the following bit values:</td></tr>
<tr><td>1</td><td>a pointer to the Exception Handler routine (invoked by <code>swi</code>, IRQs, Divide by Zero and illegal instructions (<code>bad</code>))</td></tr>
<tr><td>2</td><td>upon invocation of the Excecption Handler (see above), special register 2 will have one of four values..</td></tr>
<tr><td>3</td><td>the <code>swi</code> request number (by convention)</td></tr>
<tr><td>4</td><td>address of the supervisor mode stack on which exceptions are executed</td></tr>
<tr><td>5</td><td>return address upon entering the exception handler</td></tr>
<tr><td>6</td><td>reserved</td></tr>
<tr><td>7</td><td>reserved</td></tr>
<tr><td>8</td><td>reserved</td></tr>
<tr><td>9</td><td>an optional non-zero pointer to the Device Tree blob describing this device</td></tr>
</table>
</center>
</div>

# Instruction Set

The moxie instruction set and encoding is evolving.  Here's the
current list of instructions and encodings supported in by the moxie
toolchain.

All instructions are 16-bits long.  Some 16-bit instructions are
followed by a 32-bit immediate value.  All of the opcode space not
consumed by the encodings below is filled with the `bad` instruction.

## <table width="100%"><tr><td>`and`</td><td align='right'>`00100110AAAABBBB`</td></tr></table>
Logical and.  Performs a logical and operation on the contents of registers `$rA` and `$rB` and stores the result in `$rA`.


## <table width='100%'><tr><td>`add`</td><td align='right'>`00000101AAAABBBB`</td></tr></table>
Add, long.  Adds the contents of registers `$rA` and `$rB` and stores the result in `$rA`.
 

## <table width='100%'><tr><td>`ashl`</td><td align='right'>`00101000AAAABBBB`</td></tr></table>
Arithmetic shift left.  Performs an arithmetic shift left of `$rA` byt `$rB` bits and stores the result in `$rA`.
 

## <table width='100%'><tr><td>`ashr`</td><td align='right'>`00101101AAAABBBB`</td></tr></table>
Arithmetic shift right.  Performs an arithmetic shift right of `$rA` byt `$rB` bits and stores the result in `$rA`.
 

## <table width='100%'><tr><td>`beq`</td><td align='right'>`110000vvvvvvvvvv`</td></tr></table>
Branch if equal.  If the results of the last <code>cmp</code> demonstrated that `$rA` is equal to `$rB`, branch to the address computed by adding the signed 10-bit immediate value shifted to the left by 1 to the program counter.  The branch is relative to the start of this instruction.
 

## <table width='100%'><tr><td>`bge`</td><td align='right'>`110110vvvvvvvvvv`</td></tr></table>
Branch if greater than or equal.  If the results of the last <code>cmp</code> demonstrated that the signed 32-bit value in `$rA` is greater than or equal to the signed 32-bit value in `$rB`, branch to the address computed by adding the signed 10-bit immediate value shifted to the left by 1 to the program counter.  The branch is relative to the address of this instruction.
 

## <table width='100%'><tr><td>`bgeu`</td><td align='right'>`111000vvvvvvvvvv`</td></tr></table>
Branch if greater than or equal, unsigned.  If the results of the last <code>cmp</code> demonstrated that the unsigned 32-bit value in `$rA` is greater than or equal to the unsigned 32-bit value in `$rB`, branch to the address computed by adding the signed 10-bit immediate value shifted to the left by 1 bit to the program counter.  The branch is relative to the address of this instruction.
 

## <table width='100%'><tr><td>`bgt`</td><td align='right'>`110011vvvvvvvvvv`</td></tr></table>
Branch if greater than.  If the results of the last <code>cmp</code> demonstrated that the signed 32-bit value in `$rA` is greater than the signed 32-bit value in `$rB`, branch to the address computed by adding the signed 10-bit immediate value shifted to the left by 1 bit to the program counter.  The branch is relative to the address of this instruction.
 

## <table width='100%'><tr><td>`bgtu`</td><td align='right'>`110101vvvvvvvvvv`</td></tr></table>
Branch if greater than, unsigned.  If the results of the last <code>cmp</code> demonstrated that the unsigned 32-bit value in `$rA` is greater than the unsigned 32-bit value in `$rB`, branch to the address computed by the adding the signed 10-bit immediate value shifted to the left by 1 bit to the program counter.  The branch is relative to the address of this instruction.
 

## <table width='100%'><tr><td>`ble`</td><td align='right'>`110111vvvvvvvvvv`</td></tr></table>
Branch if less than or equal.  If the results of the last <code>cmp</code> demonstrated that the signed 32-bit value in `$rA` is less than or equal to the signed 32-bit value in `$rB`, branch to the address computed by adding the signed 10-bit immediate value shifted to the left by 1 bit to the program counter.  The branch is relative to the address of this instruction.
 

## <table width='100%'><tr><td>`bleu`</td><td align='right'>`111001vvvvvvvvvv`</td></tr></table>
Branch if less than or equal, unsigned.  If the results of the last <code>cmp</code> demonstrated that the unsigned 32-bit value in `$rA` is less than or equal to the unsigned 32-bit value in `$rB`, branch to the address computed by adding the signed 10-bit immediate value to the program counter.  The branch is relative to the address of this instruction.
 

## <table width='100%'><tr><td>`blt`</td><td align='right'>`110010vvvvvvvvvv`</td></tr></table>
Branch if less than.  If the results of the last <code>cmp</code> demonstrated that the signed 32-bit value in `$rA` is less than the signed 32-bit value in `$rB`, branch to the address computed by adding the signed 10-bit immediate value shifted to the left by 1 bit to the program counter.  The branch is relative to the address of this instruction.
 

## <table width='100%'><tr><td>`bltu`</td><td align='right'>`110100vvvvvvvvvv`</td></tr></table>
Branch if less than, unsigned.  If the results of the last <code>cmp</code> demonstrated that the unsigned 32-bit value in `$rA` is less than the unsigned 32-bit value in `$rB`, branch to the address computed by adding the signed 10-bit immediate value shifted to the left by 1 bit to the program counter.  The branch is relative to the address of this instruction.
 

## <table width='100%'><tr><td>`bne`</td><td align='right'>`110001vvvvvvvvvv`</td></tr></table>
Branch if not equal.  If the results of the last <code>cmp</code> demonstrated that `$rA` is not equal to `$rB`, branch to the address computed by adding the signed 10-bit immediate value shifted to the left by 1 bit to the program counter.  The branch is relative to the address of this instruction.
 

## <table width='100%'><tr><td>`brk`</td><td align='right'>`00110101xxxxxxxx`</td></tr></table>
Break.  The software breakpoint instruction.
 

## <table width='100%'><tr><td>`cmp`</td><td align='right'>`00001110AAAABBBB`</td></tr></table>
Compare.  Compares the contents of `$rA` to `$rB` and store the results in the processor's internal condition code register.  This is the only instruction that updates the internal condition code register used by the branch instructions.
 

## <table width='100%'><tr><td>`dec`</td><td align='right'>`1001AAAAiiiiiiii`</td></tr></table>
Decrement.  Decrement register `$rA` by the 8-bit value encoded in the 16-bit opcode.
 

## <table width='100%'><tr><td>`div`</td><td align='right'>`00110001AAAABBBB`</td></tr></table>
Divide, long.  Divides the signed contents of registers `$rA` and `$rB` and stores the result in `$rA`.  Two special cases are handled here: division by zero asserts an Divide by Zero [[Exceptions|Exception]], and INT_MIN divided by -1 results in INT_MIN.
 

## <table width='100%'><tr><td>`gsr`</td><td align='right'>`1010AAAASSSSSSSS`</td></tr></table>
Get special register.  Move the contents of the special register S into `$rA`.
 

## <table width='100%'><tr><td>`inc`</td><td align='right'>`1000AAAAiiiiiiii`</td></tr></table>
Increment.  Increment register `$rA` by the 8-bit value encoded in the 16-bit opcode.
 

## <table width='100%'><tr><td>`jmp`</td><td align='right'>`00100101AAAAxxxx`</td></tr></table>
Jump.   Jumps to the 32-bit address stored in `$rA`.  This is not a subroutine call, and therefore the stack is not updated.
 

## <table width='100%'><tr><td>`jmpa`</td><td align='right'>`00011010xxxxxxxx iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`</td></tr></table>
Jump to address.   Jumps to the 32-bit address following the 16-bit opcode.  This is not a subroutine call, and therefore the stack is not updated.
 

## <table width='100%'><tr><td>`jsr`</td><td align='right'>`00011001AAAAxxxx`</td></tr></table>
Jump to subroutine.  Jumps to a subroutine at the address stored in `$rA`.
 

## <table width='100%'><tr><td>`jsra`</td><td align='right'>`00000011xxxxxxxx iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`</td></tr></table>
Jump to subroutine at absolute address.  Jumps to a subroutine identified by the 32-bit address following the 16-bit opcode.
 

## <table width='100%'><tr><td>`ld.b`</td><td align='right'>`00011100AAAABBBB`</td></tr></table>
Load byte.  Loads the 8-bit contents stored at the address pointed to by `$rB` into `$rA`.  The loaded value is zero-extended to 32-bits.
 

## <table width='100%'><tr><td>`ld.l`</td><td align='right'>`00001010AAAABBBB`</td></tr></table>
Load long.  Loads the 32-bit contents stored at the address pointed to by `$rB` into `$rA`.
 

## <table width='100%'><tr><td>`ld.s`</td><td align='right'>`00100001AAAABBBB`</td></tr></table>
Load short.  Loads the 16-bit contents stored at the address pointed to by `$rB` into `$rA`.  The loaded value is zero-extended to 32-bits.
 

## <table width='100%'><tr><td>`lda.b`</td><td align='right'>`00011101AAAAxxxx iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`</td></tr></table>
Load absolute, byte.  Loads the 8-bit value pointed at by the 32-bit address following the 16-bit opcode into register `$rA`.  The loaded value is zero-extended to 32-bits.
 

## <table width='100%'><tr><td>`lda.l`</td><td align='right'>`00001000AAAAxxxx iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`</td></tr></table>
Load absolute, long.  Loads the 32-bit value pointed at by the 32-bit address following the 16-bit opcode into register `$rA`.
 

## <table width='100%'><tr><td>`lda.s`</td><td align='right'>`00100010AAAAxxxx iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`</td></tr></table>
Load absolute, short.  Loads the 16-bit value pointed at by the 32-bit address following the 16-bit opcode into register `$rA`.  The loaded value is zero-extended to 32-bits.
 

## <table width='100%'><tr><td>`ldi.l`</td><td align='right'>`00000001AAAAxxxx iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`</td></tr></table>
Load immediate, long.  Loads the 32-bit immediate following the 16-bit opcode into register %rA.
 

## <table width='100%'><tr><td>`ldi.b`</td><td align='right'>`00011011AAAAxxxx iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`</td></tr></table>
Load immediate, byte.  Loads the 32-bit immediate following the 16-bit opcode into register %rA.  This is a poor encoding, as the 32-bit value really only contains 8-bits of interest.
 

## <table width='100%'><tr><td>`ldi.s`</td><td align='right'>`00100000AAAAxxxx iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`</td></tr></table>
Load immediate, short.  Loads the 32-bit immediate following the 16-bit opcode into register %rA.  This is a poor encoding, as the 32-bit value really only contains 16-bits of interest.
 

## <table width='100%'><tr><td>`ldo.b`</td><td align='right'>`00110110AAAABBBB iiiiiiiiiiiiiiii`</td></tr></table>
Load offset, byte.  Loads into `$rA` the 8-bit value from memory pointed at by the address produced by adding the 16-bit value following the 16-bit opcode to `$rB`.  The loaded value is zero-extended to 32-bits.
 

## <table width='100%'><tr><td>`ldo.l`</td><td align='right'>`00001100AAAABBBB iiiiiiiiiiiiiiii`</td></tr></table>
Load offset, long.  Loads into `$rA` the 32-bit value from memory pointed at by the address produced by adding the 16-bit value following the 16-bit opcode to `$rB`.
 

## <table width='100%'><tr><td>`ldo.s`</td><td align='right'>`00111000AAAABBBB iiiiiiiiiiiiiiii`</td></tr></table>
Load offset, short.  Loads into `$rA` the 16-bit value from memory pointed at by the address produced by adding the 16-bit value following the 16-bit opcode to `$rB`.  The loaded value is zero-extended to 32-bits.
 

## <table width='100%'><tr><td>`lshr`</td><td align='right'>`00100111AAAABBBB`</td></tr></table>
Logical shift right.  Performs a logical shift right of register `$rA` by `$rB` bits and stores the result in `$rA`.
 

## <table width='100%'><tr><td>`mod`</td><td align='right'>`00110011AAAABBBB`</td></tr></table>
Modulus, long.  Compute the modulus of the signed contents of registers `$rA` and `$rB` and stores the result in `$rA`.
 

## <table width='100%'><tr><td>`mov`</td><td align='right'>`00000010AAAABBBB`</td></tr></table>
Move register to register.  Move the contents of `$rB` into `$rA`.
 

## <table width='100%'><tr><td>`mul`</td><td align='right'>`00101111AAAABBBB`</td></tr></table>
Multiply.  Multiplies the contents of registers `$rA` and `$rB` and stores the lower 32-bits of a 64-bit result in `$rA`.
 

## <table width='100%'><tr><td>`mul.x`</td><td align='right'>`00010101AAAABBBB`</td></tr></table>
Signed multiply, upper word.  Multiplies the contents of registers `$rA` and `$rB` and stores the upper 32-bits of a 64-bit result in `$rA`.
 

## <table width='100%'><tr><td>`neg`</td><td align='right'>`00101010AAAABBBB`</td></tr></table>
Negative.  Changes the sign of `$rB` and stores the result in `$rA`.
 

## <table width='100%'><tr><td>`nop`</td><td align='right'>`00001111xxxxxxxx`</td></tr></table>
Do nothing.
 

## <table width='100%'><tr><td>`not`</td><td align='right'>`00101100AAAABBBB`</td></tr></table>
Logical not.  Performs a logical not operation on the contents of register `$rB` and stores the result in register `$rA`.
 

## <table width='100%'><tr><td>`or`</td><td align='right'>`00101011AAAABBBB`</td></tr></table>
Logical or.  Performs a logical or operation on the contents of registers `$rA` and `$rB` and stores the result in `$rA`.
 

## <table width='100%'><tr><td>`pop`</td><td align='right'>`00000111AAAABBBB`</td></tr></table>
Pop the 32-bit contents of the top of the stack pointed to by `$rA` into `$rB` and update the stack pointer in `$rA`.  Stacks grown down.
 

## <table width='100%'><tr><td>`push`</td><td align='right'>`00000110AAAABBBB`</td></tr></table>
Push the contents of `$rB` onto a stack pointed to by `$rA` and update the stack pointer in `$rA`.  Stacks grown down.
 

## <table width='100%'><tr><td>`ret`</td><td align='right'>`00000100xxxxxxxx`</td></tr></table>
Return from subroutine.
 

## <table width='100%'><tr><td>`sex.b`</td><td align='right'>`00010000AAAABBBB`</td></tr></table>
Sign-extend byte.  Sign-extend the lower 8-bits of `$rB` into a `$rA` as a 32-bit value.
 

## <table width='100%'><tr><td>`sex.s`</td><td align='right'>`00010001AAAABBBB`</td></tr></table>
Sign-extend short.  Sign-extend the lower 16-bits of `$rB` into a `$rA` as a 32-bit value.
 

## <table width='100%'><tr><td>`ssr`</td><td align='right'>`1011AAAASSSSSSSS`</td></tr></table>
Set special register.  Move the contents of `$rA` into special register S.
 

## <table width='100%'><tr><td>`st.b`</td><td align='right'>`00011110AAAABBBB`</td></tr></table>
Store byte.  Stores the 8-bit contents of `$rB` into memory at the address pointed to by `$rA`.
 

## <table width='100%'><tr><td>`st.l`</td><td align='right'>`00001011AAAABBBB`</td></tr></table>
Store long.  Stores the 32-bit contents of `$rB` into memory at the address pointed to by `$rA`.
 

## <table width='100%'><tr><td>`st.s`</td><td align='right'>`00100011AAAABBBB`</td></tr></table>
Store short.  Stores the 16-bit contents of `$rB` into memory at the address pointed to by `$rA`.
 

## <table width='100%'><tr><td>`sta.b`</td><td align='right'>`00011111AAAAxxxx iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`</td></tr></table>
Store absolute, byte.  Stores the lower 8-bit contents of `$rA` into memory at the 32-bit address following the 16-bit opcode.
 

## <table width='100%'><tr><td>`sta.l`</td><td align='right'>`00001001AAAAxxxx iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`</td></tr></table>
Store absolute, long.  Stores the full 32-bit contents of `$rA` into memory at the 32-bit address following the 16-bit opcode.
 

## <table width='100%'><tr><td>`sta.s`</td><td align='right'>`00100100AAAAxxxx iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`</td></tr></table>
Store absolute, short.  Stores the lower 16-bit contents of `$rA` into memory at the 32-bit address following the 16-bit opcode.
 

## <table width='100%'><tr><td>`sto.b`</td><td align='right'>`00110111AAAABBBB iiiiiiiiiiiiiiii`</td></tr></table>
Store offset, byte.  Stores the 8-bit contents of `$rB` into memory at the address roduced by adding the 16-bit value following the 16-bit opcode to `$rA`.
 

## <table width='100%'><tr><td>`sto.l`</td><td align='right'>`00001101AAAABBBB iiiiiiiiiiiiiiii`</td></tr></table>
Store offset, long.  Stores the 32-bit contents of `$rB` into memory at the address roduced by adding the 16-bit value following the 16-bit opcode to `$rA`.
 

## <table width='100%'><tr><td>`sto.s`</td><td align='right'>`00111001AAAABBBB iiiiiiiiiiiiiiii`</td></tr></table>
Store offset, short.  Stores the 16-bit contents of `$rB` into memory at the address roduced by adding the 16-bit value following the 16-bit opcode to `$rA`.
 

## <table width='100%'><tr><td>`sub`</td><td align='right'>`00101001AAAABBBB`</td></tr></table>
Subtract, long.  Subtracts the contents of registers `$rA` and `$rB` and stores the result in `$rA`.
 

## <table width='100%'><tr><td>`swi`</td><td align='right'>`00110000xxxxxxxx iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii`</td></tr></table>
Software interrupt.  Trigger a software interrupt, where the interrupt type is encoded in the 32-bits following the 16-bit opcode.
 

## <table width='100%'><tr><td>`udiv`</td><td align='right'>`00110010AAAABBBB`</td></tr></table>
Divide unsigned, long.  Divides the unsigned contents of registers `$rA` and `$rB` and stores the result in `$rA`.
 

## <table width='100%'><tr><td>`umod`</td><td align='right'>`00110100AAAABBBB`</td></tr></table>
Modulus unsigned, long.  Compute the modulus of the unsigned contents of registers `$rA` and `$rB` and stores the result in `$rA`.
 

## <table width='100%'><tr><td>`umul.x`</td><td align='right'>`00010100AAAABBBB`</td></tr></table>
Unsigned multiply, upper word.  Multiplies the contents of registers `$rA` and `$rB` and stores the upper 32-bits of an unsigned 64-bit result in `$rA`.
 

## <table width='100%'><tr><td>`xor`</td><td align='right'>`00101110AAAABBBB`</td></tr></table>
Logical exclusive or.  Performs a logical exclusive or operation on the contents of registers `$rA` and `$rB` and stores the result in `$rA`.


## <table width='100%'><tr><td>`zex.b`</td><td align='right'>`00010010AAAABBBB`</td></tr></table>
Zero-extend byte.  Zero-extend the lower 8-bits of `$rB` into a `$rA` as a 32-bit value.
 

## <table width='100%'><tr><td>`zex.s`</td><td align='right'>`00010011AAAABBBB`</td></tr></table>
Zero-extend short.  Zero-extend the lower 16-bits of `$rB` into a `$rA` as a 32-bit value.
 
 
