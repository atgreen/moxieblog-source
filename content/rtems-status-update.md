Title: RTEMS status update
Date: 2011-06-15 04:35
Author: green
Category: moxie
Tags: RTEMS
Slug: rtems-status-update

The [RTEMS][] port in [moxiedev][] is looking pretty good right now.
Here's a test of the RTEMS network loopback device running on the moxie
gdb simulator.  The first two client connections fail in this test. 
It's supposed to fail in the first case, but I'm not sure about the
second case.   It's possible that this is just a result of there being
no pre-emptive context switching in the gdb simulator (no timers!).

    $ moxie-elf-run loopback.exe
    "Network" initializing!
    "Network" initialized!
    Try running client with no server present.
    Should fail with `connection refused'.
    Connect to server.
    Can't connect to server: Connection refused
    Client closing connection.

    Start server.

    Try running client with server present.
    Connect to server.
    Can't connect to server: Connection refused
    Client closing connection.
    Client task terminating.
    Create socket.
    Bind socket.

    Try running two clients.
    Connect to server.
    Connect to server.
    ACCEPTED:7F000001
    ACCEPTED:7F000001
    Write 22-byte message to server.
    Write 22-byte message to server.
    Read 43 from server: Server received 22 (Hi there, server (3).)
    Read 43 from server: Server received 22 (Hi there, server (2).)
    Client closing connection.
    Client task terminating.
    Client closing connection.
    Client task terminating.
    Worker task terminating.
    Worker task terminating.

    Try running three clients.
    Connect to server.
    Connect to server.
    Connect to server.
    ACCEPTED:7F000001
    ACCEPTED:7F000001
    ACCEPTED:7F000001
    Write 22-byte message to server.
    Write 22-byte message to server.
    Write 22-byte message to server.
    Read 43 from server: Server received 22 (Hi there, server (5).)
    Read 43 from server: Server received 22 (Hi there, server (6).)
    Read 43 from server: Server received 22 (Hi there, server (4).)
    Client closing connection.
    Client task terminating.
    Client closing connection.
    Client task terminating.
    Client closing connection.
    Client task terminating.
    Worker task terminating.
    Worker task terminating.
    Worker task terminating.
    *** END OF LOOPBACK TEST ***

This really needs to be tested on qemu, but I think it's time to get
back into verilog.

  [RTEMS]: http://www.rtems.com
  [moxiedev]: http://www.moxielogic.org/wiki/index.php?title=MoxieDev
