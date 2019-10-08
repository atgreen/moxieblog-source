Title: Toolchain
Date: 2017-08-27 07:53
Author: admin
Status: hidden
Slug: toolchain

# Overview

The toolchain for the moxie architecture consists of the following tools:

* the GNU assembler, linker and binary utilities
* GCC, the GNU Compiler Collection
* GDB, the GNU Debugger, including a port of the GDB simulator to the moxie architecture
* [QEMU](https://qemu.org), the Open Source Processor Emulator
* Newlib, a C library for bare-metal embedded software development

Supported target triplets include moxie-elf, moxie-rtems (for
[RTEMS](https://rtems.org) application development), and moxiebox (a
special purpose configuration for [Bloq](https://bloq.com)'s
[Ora](https://github.com/bloq/ora) bitcoin oracle
project).

# Getting and Building the Tools

## Binary Distributions

64-bit x86 DEB and RPM Linux packages for moxie-elf, moxie-rtems and
moxiebox tools are available for download.  The toolchains are
statically linked, and should run on a wide range of distributions,
including Ubuntu, Debian, Fedora, CentOS, RHEL, and more.  These
binaries track upstream development branches and are updated
frequently.

### RPM Packages

For RPMs, simply download and install the repo package here:  [https://repos.moxielogic.org:7007/MoxieLogic/noarch/moxielogic-repo-latest.rpm](https://repos.moxielogic.org:7007/MoxieLogic/noarch/moxielogic-repo-latest.rpm)

Example usage:

    $ rpm -ivh https://repos.moxielogic.org:7007/MoxieLogic/noarch/moxielogic-repo-latest.rpm
    $ yum install -y moxielogic-moxiebox-gcc moxielogic-moxiebox-gdb
    $ /opt/moxielogic/bin/moxiebox-gcc 
    moxiebox-gcc: fatal error: no input files
    compilation terminated.

### DEB Packages

For DEBs, simply add the apt repo to your system, like so:

    $ apt-add-repository https://repos.moxielogic.org:7114/MoxieLogic moxiedev main

Example usage:

    $ apt-add-repository https://repos.moxielogic.org:7114/MoxieLogic moxiedev main
    $ apt-get install -y moxielogic-moxiebox-gcc moxielogic-moxiebox-gdb
    $ /opt/moxielogic/bin/moxiebox-gcc 
    moxiebox-gcc: fatal error: no input files
    compilation terminated.

## Source Distributions

The [moxiedev-releng](https://github.com/atgreen/moxiedev-releng) git
repo provides scripts and tools required to rebuild these binaries
from source.

The RPM repo includes source RPMs from which all of the tools are
built.  The DEB packages are converted from RPM using
[alien](https://en.wikipedia.org/wiki/Alien_(software)).








