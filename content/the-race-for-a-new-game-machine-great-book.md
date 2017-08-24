Title: The Race For A New Game Machine: great book!
Date: 2009-05-15 21:19
Author: green
Category: Uncategorized
Slug: the-race-for-a-new-game-machine-great-book

I just read [The Race For A New Game Machine][] today on a cross-country
flight, and wow.. fun read!

If you've ever read Tracy Kidder's great book [The Soul of a New
Machine][], you'll know what to expect. But this book chronicles the
SONY/Toshiba/IBM [Cell][] partnership, and the creation of the processor
core at the heart of both the PS3 and XBOX360 from the point of view of
lead architect David Shippy. Not only is it full of interesting
technical details\*\*, but it exposes a dark story of manipulation,
deception, betrayal and broken friendships. Some of the story is so
strange it's hard to believe.

Many years ago I was involved in a some work with Toshiba and SONY
around the [Emotion Engine][], the MIPS-based core used in the
PlayStation 2. The team at Cygnus/Red Hat had done lots of work on PS2
development tools, and we all liked working with the Toshiba and SCEI
people. It was disappointing to learn that we weren't going to
participate in the Cell project but, after reading this, maybe it was
for the best!

\*\* This book introduced me to [clock gating][], a trick used by ASIC
developers to save power. Shippy's core passed a "power token" through
the processor pipeline, ensuring that at any one time the only pipeline
logic being clocked was the logic being used. Neat trick, but apparently
the savings aren't that great for FPGAs.

  [The Race For A New Game Machine]: http://raceforxbox360ps3.com/default.aspx
  [The Soul of a New Machine]: http://en.wikipedia.org/wiki/The_Soul_of_a_New_Machine
  [Cell]: http://en.wikipedia.org/wiki/Cell_(microprocessor)
  [Emotion Engine]: http://en.wikipedia.org/wiki/Emotion_Engine
  [clock gating]: http://en.wikipedia.org/wiki/Clock_gating
