Title: Using the Altera USB-Blaster on Fedora
Date: 2011-10-28 13:14
Author: green
Category: moxie
Tags: Altera, de2, JTAG, Quartus
Slug: using-the-altera-usb-blaster-on-fedora

Altera's Quartus tools include some special software to download
bitstreams to their devices over USB (a DE-2 eval board, in my case).
They require some tricky work to set up properly on Fedora - my dev host
of choice. But you're in luck! I've packaged up an RPM that takes care
of this extra work for you. It creates a udev rule to set up the
USB-Blaster properly when you plug in your USB JTAG connection. It also
provides a service wrapper for Altera's jtagd daemon and moves some of
Altera's data files around so things just work. The sources are in
[moxiedev][], but I've posted the binary and source RPMs here for
convenience: <http://moxielogic.org/tools/>. Be sure to read the docs in
`/usr/share/doc/moxie-quartus-altera-1` once installed. It assumes that
you've already installed Quartus II on your box (they don't package in
RPM format, unfortunately).

I'm told that the open source alternative [UrJTAG][] may work for this
device as well, but I haven't had a chance to look into it. Any
experience worth sharing out there?

  [moxiedev]: http://github.com/atgreen/moxiedev "moxiedev"
  [UrJTAG]: http://urjtag.org/ "urjtag"
