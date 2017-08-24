Title: Moxie on Altera's Cyclone II, and a Chance Encounter
Date: 2013-08-08 18:59
Author: green
Category: moxie
Tags: Altera, de2, marin, qemu, Quartus
Slug: moxie-on-alteras-cyclone-ii-and-a-chance-encounter

I recently fired up the Altera software, Quartus II, and spent a little
time porting the Marin SoC to the popular Cyclone II based DE2 board.
There's no external memory support yet, but on-chip memory is working,
and it looks like the on-chip bootloader is coming up properly. As
usual, everything has been committed to github at
<http://github.com/atgreen/moxie-cores>.

I was riding the subway to a meeting downtown today after a late night
of messing around with Quartus II when I noticed a guy with an Altera
bag sitting next to me --- the Baader-Meinhof phenomenon in action! So I
struck up a conversation, and it turns out he works on the Quartus II
place-and-route software here in the Toronto office. Small world!

Also, I just noticed something extremely cool in Fedora rawhide (the
incubator that will produce Fedora 20):
'`yum install qemu-system-moxie`\` works! It's packaged up as part of
the latest QEMU release in Fedora.
