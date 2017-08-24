Title: NetHack in your browser
Date: 2014-01-26 18:12
Author: green
Category: moxie
Tags: gdb, NetHack, RTEMS
Slug: nethack-in-your-browser

This is a moxie-rtems port of NetHack running on a modified version of
the gdb moxie simulator compiled to javascript with [emscripten][].


<canvas id="tty" class="screen" width="640" height="384">
                        Terminal uses canvas
                    </canvas>
<script src="http://kl7107.github.io/moxie-sim/c/terminal.js"></script>
<script src="http://kl7107.github.io/moxie-sim/c/terminal-input.js"></script>
<script src="http://kl7107.github.io/moxie-sim/c/moxie.js"></script>
<script src="http://kl7107.github.io/moxie-sim/c/nethack.js"></script>
                        
[Krister Lagerström][] is responsible for this marvellous hack.

Also, I suppose this blog entry represents a distribution of some GPL'd
source code from GDB, so I need to tell you about the:

-   [Source Code][]
-   [License][]
-   [Song][]

And then there's RTEMS:

-   [Source][]
-   [License][1]

And finally NetHack:

-   [Source][2]
-   [License][3]

  [emscripten]: https://github.com/kripken/emscripten "emscripten"
  [Krister Lagerström]: http://github.com/kl7107
  [Source Code]: https://github.com/kl7107/moxie-sim
  [License]: http://www.gnu.org/licenses/
  [Song]: http://www.gnu.org/music/gdb-song.html
  [Source]: http://github.com/atgreen/RTEMS
  [1]: http://www.rtems.org/license
  [2]: https://github.com/kl7107/nethack-moxie
  [3]: http://www.nethack.org/common/license.html
