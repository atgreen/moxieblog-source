Title: New git repo
Date: 2009-05-26 20:05
Author: green
Category: moxie
Tags: releng, u-boot
Slug: new-git-repo

I'll bottom line this one quickly:

-   [moxiedev][] is now maintained with git. Check it out like so..  
    `$ git clone http://moxielogic.org/moxiedev.git`
-   moxiedev now contains a partial [u-boot port][]. It's "partial"
    because I fat fingered some commands and blew away four or five
    important files. They will have to be recreated before this thing
    builds.

Lessons learned:

-   hg is much more intuitive than git. Unfortunately hg and/or my hg
    hoster was having problems with the size of moxiedev, necessitating
    a change. Hosting a public git repo on my own system seemed like the
    easiest thing.
-   Make sure you backup ***everything***. I am cursing myself for not
    having pushed out the u-boot port much sooner (but I had to move off
    of the hg system first).

BTW - still waiting on GCC steering committee decision on inclusion of
moxie port.

  [moxiedev]: http://moxielogic.org/wiki/index.php?title=MoxieDev
  [u-boot port]: http://moxielogic.org/blog/?p=154
