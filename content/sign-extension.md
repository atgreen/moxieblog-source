Title: Sign Extension
Date: 2014-04-04 00:40
Author: green
Category: moxie
Slug: sign-extension

Moxie zero-extends all 8 and 16-bit loads from memory. Until recently,
however, the GCC port didn't understand how loads worked, and would
always shift loaded values back and forth to either empty out the upper
bits or sign-extend the loaded value. While correct, it was overly
bloated. If we're loading an unsigned char into a register, there's no
need to force the upper bits to clear. The hardware does this for us.

For instance, this simple C code....

<p>
<script src="https://gist.github.com/atgreen/9970355.js"></script>
</p>
..would compile to...

<p>
<script src="https://gist.github.com/atgreen/9970378.js"></script>
</p>
Thanks to help from hackers on the [GCC mailing list][], I was finally
able to teach the compiler how to treat memory loads correctly. This led
to two changes...

1.  The introduction of 8 and 16-bit sign extension instructions
    (`sex.b` and `sex.s`). Sometimes we really do need to sign-extend
    values, and logical shift left followed by arithmetic shift right is
    a pretty expensive way to do this on moxie.
2.  The char type is now unsigned by default. If you have zero-extending
    8-bit loads then you had better make your char type unsigned,
    otherwise your compiler output will be littered with sign extension
    instructions.

<p>
Now for the C code above, we get this nice output....  

<script src="https://gist.github.com/atgreen/9970471.js"></script>
</p>
I believe that this was the last major code quality issue from the GCC
port, and the compiler output should be pretty good now

I've updated the upstream GCC, binutils and gdb (sim) repositories, my
[QEMU][] fork in github, as well as the MoxieLite VHDL core in the
[moxie-cores][] git repo.

  [GCC mailing list]: http://gcc.gnu.org/ml/gcc/2014-04/msg00008.html
  [QEMU]: http://github.com/atgreen/qemu-moxie
  [moxie-cores]: http://github.com/atgreen/moxie-cores
