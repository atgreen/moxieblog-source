Title: Moxiebox and bitcoin
Date: 2014-12-18 05:00
Author: green
Category: moxie
Tags: moxiebox, bitcoin
Slug: moxiebox-and-bitcoint

<center>
![http://bitcoin.org](http://moxielogic.org/images/Bitcoin-logo.jpg)
</center>

One of the more interesting developments around moxie is the adoption
of the [moxie
architecture](http://moxielogic.org/blog/pages/architecture.html) by
the core bitcoin developers ([Jeff
Garzik](http://garzikrants.blogspot.ca/), in particular), for an
experimental project called
[`moxiebox`](http://github.com/jgarzik/moxiebox).

To quote Jeff...

> The goal is to provide a secure, sandboxed execution mechanism that enables deterministic input, processing and output. Execution is separated out into distinct phases:

>  1. Prepare and load hash-sealed program executables, data.
>  2. Execute program as a black box, with no I/O capability. Runs until exit or CPU budget exhausted (or CPU exception).
>  3. Gather processed data, if any.

> A single thread of execution pre-loads necessary data, then simulates a 32-bit little endian Moxie CPU, running the loaded code.

I don't pretend to have deep understand bitcoin technology, but my
basic understanding is that moxiebox could be used to implement
automated smart contracts.  For instance, signed moxiebox executables
controlling a certain number of bitcoins could be distributed in the
[block chain](http://en.wikipedia.org/wiki/Bitcoin#The_block_chain).
These programs would decide what to do with the bitcoins based on
program execution against certain input.  People could independently
verify the results of this program because it's all designed to be
completely deterministic and reproducible.

From a moxie tooling perspective, I added a moxiebox target to the GNU
toolchain to simplify its use.  The moxiebox project supplies the
simulator, as well as crt0 and some custom moxie runtime libraries.
The 'moxiebox-gcc' compiler is configured to link everything in the
right order, including newlib, the custom crt0 and sandbox runtime
library.

It's not clear how things will develop, but one thing that's come up
is extending the moxie ISA to include new instructions in support of
crypto activities.  We'll just have to see.  You can follow along at
[http://github.com/jgarzik/moxiebox](http://github.com/jgarzik/moxiebox).



