Title: Toolchain
Date: 2015-01-29 06:38
Author: admin
Status: hidden
Slug: toolchain

# Overview

The toolchain for the moxie architecture consists of the following tools:

* the GNU assembler, linker and binary utilities
* GCC, the GNU Compiler Collection
* GDB, the GNU Debugger, including a port of the GDB simulator to the moxie architecture
* [QEMU](http://qemu.org), the Open Source Processor Emulator
* Newlib, a C library for bare-metal embedded software development

Supported target triplets include moxie-elf, moxie-rtems (for
[RTEMS](http://rtems.org) application development), and moxiebox (a
special purpose configuration for the
[moxiebox](http://github.com/jgarzik/moxiebox) bitcoin oracle
project).

# Getting and Building the Tools

## Binary Distributions

Signed packages for moxie-elf, moxie-rtems and moxiebox are available
for Fedora, CentOS and RHEL.  Simply download and install the
appropriate repo package below:

* [Fedora 20 x86_64](http://184.106.241.209/yum/MoxieLogic/f20/RPMS/noarch/moxielogic-repo-f20-1-5.noarch.rpm)
* [Fedora 21 x86_64](http://184.106.241.209/yum/MoxieLogic/f21/RPMS/noarch/moxielogic-repo-f21-1-5.noarch.rpm)
* [CentOS/RHEL 6](http://184.106.241.209/yum/MoxieLogic/el6/RPMS/noarch/moxielogic-repo-el6-1-5.noarch.rpm)
* [CentOS/RHEL 7](http://184.106.241.209/yum/MoxieLogic/el7/RPMS/noarch/moxielogic-repo-el7-1-5.noarch.rpm)

The fingerprint for the signing key is `1D94 EA73 7436 1929 B906  804C 89D7 255C BFE9 22AD`.

Example usage:

    $ rpm -ivh http://184.106.241.209/yum/MoxieLogic/el7/RPMS/noarch/moxielogic-repo-el7-1-5.noarch.rpm
    $ yum install -y moxielogic-moxiebox-gcc moxielogic-moxiebox-newlib moxielogic-moxiebox-gdb
    $ /opt/moxielogic/bin/moxiebox-gcc 
    moxie-elf-gcc: fatal error: no input files
    compilation terminated.


## Source Distributions

The [moxie-cores](http://github.com/atgreen/moxie-cores) project
provides scripts to download and build the toolchain on Linux hosts.
See the tools directory for the
[download](https://raw.githubusercontent.com/atgreen/moxie-cores/master/tools/download-tools-sources.sh)
and
[build](https://raw.githubusercontent.com/atgreen/moxie-cores/master/tools/build-elf-tools.sh)
scripts.






