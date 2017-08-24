Title: The first moxie linux boot output...
Date: 2009-07-26 12:43
Author: green
Category: moxie
Tags: linux
Slug: the-first-moxie-linux-boot-output

Userland, here I come! Check out [moxiedev][], run "ant build", then do
the following...

    $ ./root/usr/bin/moxie-elf-run linux-2.6/vmlinux
    Linux version 2.6.31-rc3-gb006656-dirty (green@dev.moxielogic.com) (gcc version 4.5.0 20090715 (experimental) [trunk revision 149693] (GCC) ) #6 Sun Jul 26 12:03:14 EDT 2009
    console [earlyser0] enabled
    setup_cpuinfo: initialising
    setup_memory: Main mem: 0x0-0x1000000, size 0x01000000
    setup_memory: kernel addr=0x00001000-0x002cc000 size=0x002cb000
    setup_memory: max_mapnr: 0x1000
    setup_memory: min_low_pfn: 0x0
    setup_memory: max_low_pfn: 0x1000
    On node 0 totalpages: 4096
    free_area_init_node: node 0, pgdat 002621b0, node_mem_map 002cd000
      Normal zone: 32 pages used for memmap
      Normal zone: 0 pages reserved
      Normal zone: 4064 pages, LIFO batch:0
    Built 1 zonelists in Zone order, mobility grouping off.  Total pages: 4064
    Kernel command line: lpj=1000
    PID hash table entries: 64 (order: 6, 256 bytes)
    Dentry cache hash table entries: 2048 (order: 1, 8192 bytes)
    Inode-cache hash table entries: 1024 (order: 0, 4096 bytes)
    Memory: 13376k/16384k available
    start_kernel(): bug: interrupts were enabled *very* early, fixing it
    NR_IRQS:32
     #0 at 0x00000000, num_irq=0, edge=0x0
     #0 at 0x00000000, irq=0
    start_kernel(): bug: interrupts were enabled early
    ODEBUG: 3 of 3 active objects replaced
    ODEBUG: selftest passed
    Calibrating delay loop (skipped) preset value.. 0.20 BogoMIPS (lpj=1000)
    Mount-cache hash table entries: 512
    NET: Registered protocol family 16
    bio: create slab  at 0
    NET: Registered protocol family 2
    IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
    TCP established hash table entries: 512 (order: 0, 4096 bytes)
    TCP bind hash table entries: 512 (order: -1, 2048 bytes)
    TCP: Hash tables configured (established 512 bind 512)
    TCP reno registered
    NET: Registered protocol family 1
    ROMFS MTD (C) 2007 Red Hat, Inc.
    msgmni has been set to 26
    io scheduler noop registered
    io scheduler anticipatory registered
    io scheduler deadline registered
    io scheduler cfq registered (default)
    brd: module loaded
    nbd: registered device at major 43
    uclinux[mtd]: RAM probe address=0x2cba18 size=0x0
    Creating 1 MTD partitions on "RAM":
    0x000000000000-0x000000000000 : "ROMfs"
    mtd: partition "ROMfs" is out of reach -- disabled
    TCP cubic registered
    NET: Registered protocol family 17
    RPC: Registered udp transport module.
    RPC: Registered tcp transport module.
    VFS: Cannot open root device "" or unknown-block(0,0)
    Please append a correct "root=" boot option; here are the available partitions:
    Rebooting in 120 seconds..
    Machine restart...

    Stack:
      00823e50 00823e68 000044e6 fffffff3 002288e0 fa3c0600 00823e7c 0001e196 
      19981fc0 00000000 0001d4bf 00823ec0 0003ef30 00000000 00229ba8 00000078 
      00000000 19981fc0 00000000 0003ef84 000fe422 0007091a 00008001 00000018 
    Call Trace: 

    [<000044e6>] machine_restart+0x14/0x1a
    [<0001e196>] emergency_restart+0xe/0x10
    [<0001d4bf>] sys_rt_sigtimedwait+0x15/0x1de
    [<0003ef30>] panic+0x11e/0x172
    [<0003ef84>] printk+0x0/0x1a
    [<000fe422>] strchr+0x0/0x4a
    [<0007091a>] sys_mount+0x0/0xf4
    [<00008001>] update_curr.clone.4+0x115/0x178
    [<0003ef84>] printk+0x0/0x1a
    [<00266bca>] mount_block_root+0x2d0/0x2f4
    [<00008001>] update_curr.clone.4+0x115/0x178
    [<00266d94>] mount_root+0x7c/0x86
    [<00266f38>] prepare_namespace+0x19a/0x1e6
    [<00001314>] do_one_initcall+0x0/0x280
    [<00001314>] do_one_initcall+0x0/0x280
    [<002667ba>] kernel_init+0xea/0x104
    [<000025c8>] kernel_thread_helper+0x8/0x14
    [<002666d0>] kernel_init+0x0/0x104
    [<000025c0>] kernel_thread_helper+0x0/0x14

    program stopped with signal 2.

There are lots of short cuts that need to be cleaned up, but it seems
that I'm basically at the point where I need to worry about userland.

**[Busybox][], I'm looking at you!**

  [moxiedev]: http://moxielogic.org/wiki/index.php?title=MoxieDev
  [Busybox]: http://www.busybox.net
