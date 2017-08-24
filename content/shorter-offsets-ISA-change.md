Title: Compacting the code with shorter load/store offsets
Date: 2014-12-28 08:47
Author: green
Category: moxie
Tags: moxie, architecture
Slug: shorter-load-store-offsets

You may recall that moxie supports two instructions lengths: 16- and 48-bit.
Today I'm introducing a few 32-bit instructions as well.

Previously, moxie's "load and store with offset" instructions were
defined as...

<blockquote>
<table width='100%'><tr><td><b>ldo.l</b></td><td align='right'><b>00001100AAAABBBB iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii</b></td></tr></table>
Load offset, long.  Loads into <b>$rA</b> the 32-bit value from memory pointed at by the address produced by adding the 32-bit value following the 16-bit opcode to <b>$rB</b>.
<p>
<table width='100%'><tr><td><b>sto.l</b></td><td align='right'><b>00001101AAAABBBB iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii</b></td></tr></table>
Store offset, long.  Stores the 32-bit contents of <b>$rB</b> into memory at the address roduced by adding the 32-bit value following the 16-bit opcode to <b>$rA</b>.
</blockquote>

In addition to these two, there are versions to load and store 16- and
8-bit values.

In almost every `ldo` and `sto` case, however, the upper 16 bits of
the offset were either 0x0000 or 0xFFFF (for negative offsets).
You'll see a lot of these when we access local C variables accessed by
indexing off of `$fp`.

Shortening the offset from 32 to 16 bits has always been on my radar
but I was slow to implement because it's a backwards-incompatible
change, and focus has been on tool/core correctness - not
optimization.  But now it's time to clean things up, and I've
implemented this change in all of the upstream moxie tools.  I'm also
testing a MoxieLite core change as well and should be pushing it to
github shortly.

The new ldo and sto instructions look like this (for example)...

<blockquote>
<table width='100%'><tr><td><b>ldo.l</b></td><td align='right'><b>00001100AAAABBBB iiiiiiiiiiiiiiii</b></td></tr></table>
Load offset, long.  Loads into <b>$rA</b> the 32-bit value from memory pointed at by the address produced by adding the 16-bit value following the 16-bit opcode to <b>$rB</b>.
<p> 
<table width='100%'><tr><td><b>sto.l</b></td><td align='right'><b>00001101AAAABBBB iiiiiiiiiiiiiiii</b></td></tr></table>
Store offset, long.  Stores the 32-bit contents of <b>$rB</b> into memory at the address roduced by adding the 16-bit value following the 16-bit opcode to <b>$rA</b>.
</blockquote>




