Title: The Moxielyzer
Date: 2009-10-14 22:05
Author: green
Category: moxie
Tags: architecture, moxielyzer
Slug: the-moxielyzer

I just committed a little binary analysis tool to [moxiedev][]. You can
use it to perform simple static analysis on moxie binaries. The kinds of
things I'm looking for are compiler bugs (because I know there's still
one there that is triggered by -frerun-cse-after-loop), and instruction
statistics. For instance, which registers are used as load offsets, and
how often? The tool uses a primitive plugin architecture that should
make it easy to add new analysis tools in the future. It's called the
moxielyzer, and here is the [initial commit][]. Run it with no arguments
to get a list of plugins. Run it with just a plugin name, and it will
describe the plugin. Run it with a plugin name as well as an ELF moxie
executable filename, and the analysis will be performed.

I had written a similar tool for ggx back in the bad old days. Another
option was to hack this stuff into gas, but I prefer to keep gas "clean"
(translation: I want the freedom to maintain hacky analysis code).

BTW - I'm also rolling out a new [libffi][] in a few weeks. You can keep
track of the release candidate test results [on the wiki here][].

  [moxiedev]: http://moxielogic.org/wiki/index.php?title=MoxieDev
  [initial commit]: http://github.com/atgreen/moxiedev/commit/150f230a2f4a2084e277b89dde846ca02f9ccc12
  [libffi]: http://sourceware.org/libffi/
  [on the wiki here]: http://moxielogic.org/wiki/index.php?title=Libffi_3.0.9
