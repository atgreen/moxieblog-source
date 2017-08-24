Title: Forking bugs
Date: 2012-08-15 20:59
Author: green
Category: moxie
Tags: linux
Slug: forking-bugs

I found some time to look at the Linux kernel port again, and discovered
a bug in the forking code (the child process must return 0 after a
fork!). What we're looking at here is the start of userland, post kernel
boot, where busybox is trying to run an init script. It's still not
working, but some cool things are, like the stack trace. I think the
next troubling bit is where busybox tries to exec itself
(/proc/self/exe) and /proc isn't mounted. Or something like that.

    ___  ___           _              _____ _ _                  
    |  \/  |          (_)            /  __ \ (_)                 
    | .  . | ___ __  ___  ___   _   _| /  \/ |_ _ __  _   ___  __
    | |\/| |/ _ \\ \/ / |/ _ \ | | | | |   | | | '_ \| | | \ \/ /
    | |  | | (_) |>  <| |  __/ | |_| | \__/\ | | | | | |_| |>  < 
    \_|  |_/\___//_/\_\_|\___|  \__,_|\____/_|_|_| |_|\__,_/_/\_\
    sh: can't execute 'ls': No such file or directory.
    /bin/sh: option requires an argument -- c
    BusyBox v1.19.0.git (2012-08-14 23:32:21 EDT) multi-call binary.

    Usage: sh [-nxl] [-c 'SCRIPT' [ARG0 [ARGS]] / FILE [ARGS]]

    Unix shell interpreter

    Kernel panic - not syncing: Attempted to kill init!
    Rebooting in 120 seconds..
    Machine restart...

    Stack:
      03819e8c ffffffff 03819fb8 ffffffff ffffffff 03819ec0 0000408a 000fdfd2 
      0022438c 00000063 fa3c0000 00000000 00000000 03819ee4 03819ee4 0001e800 
      03bb8d14 0002990e ffffffff ffffffff 000003e8 000fceac 0001d4bf 03819f34 
    Call Trace: 

    [<0000408a>] machine_restart+0x14/0x1a
    [<000fdfd2>] bust_spinlocks+0x0/0x4a
    [<0001e800>] emergency_restart+0xa/0xc
    [<0002990e>] up_read+0x8/0xa
    [<000fceac>] __muldi3+0x0/0x92
    [<0001d4bf>] do_notify_parent+0x193/0x240
    [<0004038c>] panic+0x11c/0x162
    [<00012ea8>] exit_files+0x1e/0x26
    [<000130c6>] do_exit+0x6e/0x706
    [<0001377a>] sys_exit+0x0/0x18
    [<00013792>] do_group_exit+0x0/0xac
    [<00057fe2>] sys_write+0x0/0x96
    [<000017fa>] .return_from_exception+0x0/0x18
