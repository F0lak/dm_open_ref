## background setting (proc)
**See also:**
*   [sleep proc](/ref/proc/sleep.md) -m
*   [spawn proc](/ref/proc/spawn.md) -m

To avoid lag from procedures that hog the CPU for too long, you
can turn on background processing. This will cause it to periodically
sleep for long enough to allow other events to be processed.


The following example is a typical \"ticker\" procedure. It
spawns off an infinite loop which does some work and then sleeps before
iterating again. By running this in the background, you ensure that the
work being done does not create large delays. You could achieve a
similar thing by sprinkling calls to sleep(0) or sleep(-1) in the
\"working\" part of the loop.
### Example

```
 proc/Ticker() set background = 1 spawn while(1) for(var/mob/M
in world) M.Tick() sleep(10) 
```
 

Since the background
procedure sleeps at unpredictable times, you must be aware that race
conditions are possible if the background procedure interacts with
variables modified by other procedures. It\'s still much safer than
multi-threaded programs because the background procedure never
interrupts other code; but other code may interrupt the background
procedure. 

Note that procedures that are called by the
background procedure do not automatically run in the background unless
they too have the background setting turned on. For instance, the code
in the above example does not imply that the mob Tick() procs would run
in the background. This is convenient, because you should only ever
apply background processing to code after checking that there are no
potential race conditions involved. 

If you have an eye for race
conditions, you might think that the above code has one in which a mob
gets deleted after it is assigned to M but before the call to M.Tick()
is executed. However, *background processing is only interrupted at loop
points in the code*, so the above code is safe. It would only ever be
interrupted at the end of the `for` or `while` loops.