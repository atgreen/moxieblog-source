Title: Bisecting GCC
Date: 2011-06-06 07:23
Author: green
Category: moxie
Tags: ec2, gcc, git
Slug: bisecting-gcc

The thing about [GCC][] is that things break when you take your eye off
the ball. And this is what happened during my months long hiatus from
the moxie project. Somewhere between early March and today, the moxie
GCC port lost the ability to compile non-trivial code, notably libgcc.
Firing up gdb on a core file may have been illuminating to somebody who
lived in GCC sources every day but, to the occasional hacker, it's
difficult to see where things went wrong if you don't know what you're
looking for. Enter [git bisect][]...

The git bisect tool automates finger pointing by binary searching
through your source history for offending patches. It needs three things
to work:

1.  An older known working version of the sources.
2.  A newer known broken version of the sources.
3.  A test executable (typically a shell script) that will tell whether
    a given version of the source code is broken or not.

Given all this, git bisect will start a binary search through the git
history for your code, looking for the exact commit that caused the test
to fail.

The test case I used was to build moxie's C compiler and try to compile
one of the libgcc sources that fails. If the compiler doesn't report an
error, we're good, otherwise we know we still have the bug. Here's the
script I used as the git bisect test:  

    #!/bin/sh

    # My git clone of the gcc tree
    GCCSRC=~/bisect/gcc

    # My pre-processed test case
    TESTSRC=~/bisect/test.i

    cd ~/bisect

    rm -rf build
    mkdir build

    (cd build;
     $GCCSRC/configure --target=moxie-elf --enable-languages=c;
     make -j8 all-gcc)

    if test -f build/gcc/cc1; then
      # build my test case
      build/gcc/cc1 -O2 $TESTSRC;
      # cc1 returns exit codes outside of git's acceptable range, so...
      if test "$?" -ne "0"; then
        exit 1;
      fi;
      exit 0;
    else
      exit 1;
    fi

Note that GCC is maintained in a [subversion tree][], but there's an
official [git mirror][] that makes all of this possible. You need to
clone it locally before you can do anything.

There were over 1000 commits between my last known working version and
today's GCC sources. My first thought was... "this is going to take
hours". I was wrong.

Running "`git bisect run ~/bisect/test.sh`" took all of 35 minutes.

The smartest thing I did here was work on a [large amazon ec2
instance][]. It's a cloud-hosted virtual server similar to a dual-core
system with 7GB RAM and ample fast storage all for about 34 cents an
hour. I've taken to doing development in the cloud and, relative to my
standard setup, it is blazingly fast! I created a Fedora 15 image, yum
installed all my tools (don't forget [ccache][]!), git cloned
[moxiedev][], gcc and my [emacs config][] files, and I was bisecting in
no time.

Git bisect told me that on Monday, March 21, my old colleague Richard
Sandiford committed some [improvements to GCC][] that were tripping up
the moxie port. A few minutes later I caught up with Richard on [IRC][],
where he explained the patch to me. Shortly after this I'm testing a
fix. Amazing.

  [GCC]: http://gcc.gnu.org
  [git bisect]: http://www.kernel.org/pub/software/scm/git/docs/git-bisect.html
  [subversion tree]: http://gcc.gnu.org/svn.html
  [git mirror]: http://gcc.gnu.org/wiki/GitMirror
  [large amazon ec2 instance]: http://aws.amazon.com/ec2/instance-types/
  [ccache]: http://ccache.samba.org/
  [moxiedev]: http://github.com/atgreen/moxiedev
  [emacs config]: http://github.com/atgreen/emacs
  [improvements to GCC]: http://gcc.gnu.org/ml/gcc-patches/2011-03/msg01344.html
  [IRC]: http://gcc.gnu.org/wiki/GCConIRC
