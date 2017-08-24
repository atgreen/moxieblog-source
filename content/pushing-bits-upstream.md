Title: Pushing Bits Upstream
Date: 2009-04-16 17:55
Author: green
Category: moxie
Tags: binutils
Slug: pushing-bits-upstream

If there's one thing I've learned about GNU tools development over the
years, it's that attempting to maintain a tools port outside of the
upstream tree is A Very Bad Idea! It's easy to let your private tree
fall out of sync from upstream. And the longer you wait to fix things,
the more expensive it becomes.

![img00017-20090402-12411][]

So a few weeks ago I submitted my copyright assignment forms to the
[FSF][] -- an important precondition to getting any port accepted
upstream. Although there's some debate over the value of a having a
single copyright holder for Free Software projects, I trust that the
Free Software Foundation will continue to be an excellent steward of the
GNU toolchain. And, when it comes down to it, there's little choice if
you are interested in participating in GNU tools development.

Last night I [submitted the moxie binutils port][] to the binutils
mailing list, and earlier today Nick Clifton [accepted them][] and
merged them into the upstream src tree! GCC and newlib are next.

  [img00017-20090402-12411]: http://moxielogic.org/blog/wp-content/uploads/2009/04/img00017-20090402-12411-300x225.jpg
    "img00017-20090402-12411"
  [FSF]: http://www.fsf.org
  [submitted the moxie binutils port]: http://sourceware.org/ml/binutils/2009-04/msg00211.html
  [accepted them]: http://sourceware.org/ml/binutils/2009-04/msg00229.html
