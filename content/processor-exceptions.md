Title: Processor Exceptions
Date: 2009-04-02 08:33
Author: green
Category: moxie
Tags: architecture
Slug: processor-exceptions

My first go at exceptions is working well. The basic idea is that moxie
will have a single exception handling routine whose address lives in
special register 1. You set the exception handler like so:

    void install_handler(void (*handler)(void))
    {
      printf ("Installing handler 0x%x\n", (unsigned) handler);
      asm("ssr %0, 1" : : "r" (handler));
    }

When the processor hits an exception, it performs a standard function
call to the handler. We return from the handler just like it was any old
function, since it currently uses the standard C ABI. The exception type
will be found in special register 2. The current exception types are as
follows:

    #define MOXIE_EX_DIV0 0 /* Divide by zero */
    #define MOXIE_EX_BAD  1 /* Illegal instruction */
    #define MOXIE_EX_IRQ  2 /* Interrupt request */
    #define MOXIE_EX_SWI  3 /* Software interrupt */

In the case of IRQ and SWI exceptions, the interrupt number will be
found in special register 3. I don't have instructions yet to disable or
enable interrupts, but those are an obvious next step. Here's a sample
exception handler:

    void handler (void)
    {
      int et;

      /* Get the exception handler from special register 2.  */
      asm("gsr %0, 2" : "=r"(et) : "0"(et) );

      switch (et)
        {
        case MOXIE_EX_DIV0:
          printf("DIVIDE BY ZERO EXCEPTION\n");
          break;
        case MOXIE_EX_BAD:
          printf("ILLEGAL INSTRUCTION EXCEPTION\n");
          break;
        case MOXIE_EX_IRQ:
          {
            int irq;
            asm("gsr %0, 3" : "=r"(irq) : "0"(irq) );
            printf("INTERRUPT REQUEST %d\n", irq);
          }
          break;
        case MOXIE_EX_SWI:
          {
            int swi;
            asm("gsr %0, 3" : "=r"(swi) : "0"(swi) );
            printf("SOFTWARE INTERRUPT REQUEST %d\n", swi);
          }
          break;
        default:
          printf("UNKNOWN EXCEPTION 0x%x\n", et);
          break;
        }
    }

The handler for DIV0 and SWI may also want to know where the exception
happened. This can be determined by pulling the return address off of
the stack and subtracting the appropriate instruction length (2 for div
and 6 for swi).

I've implemented support for this in the qemu port, and the test
directory in moxiedev contains a simple program to exercise this new
functionality. I think we'll want to hook up some peripherals in qemu to
the IRQ system soon.
