Title: GTKWave Tip #2: Translate Filter Files
Date: 2011-10-06 17:10
Author: green
Category: moxie
Tags: gtkwave
Slug: gtkwave-tip-2-translate-filter-files

Tip \#1 was about using an external process to perform dynamic
translations of signal display values. GTKWave can also perform simple
static translations of data. In the example below, for instance, moxie's
execute unit is receiving a 4-bit signal identifying "register A"
(riA\_i) for whatever operation is about to happen. This waveform would
normally just show "0", "1", "2", etc. We can replace those values by
using a simple filter file that maps those string representations to
alternate values. Here's the one I use for register names:
[gtkwave-regs.txt][]. After applying the filter we see the register name
"$r1" instead of its register file index value of "2".. a tremendous
readability improvement!  
<center>
![gtkwave with moxie register name translation filter file][1]
</center>

  [gtkwave-regs.txt]: https://github.com/atgreen/moxiedev/blob/master/moxie/soc/muskoka/gtkwave/gtkwave-regs.txt
  [1]: http://moxielogic.org/blog/wp-content/uploads/2011/10/Screenshot-GTKWave-dump.vcd-1.png    "Screenshot-GTKWave - dump.vcd-1"
