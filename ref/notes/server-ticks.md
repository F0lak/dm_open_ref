## Server Ticks

A server tick represents the period between one TimeLib_TickServer() call and the next.
To make it easier to understand how BYOND works, this breakdown is provided to help you
understand the work the server does every tick. The following is in the same order as these
events occur each tick.

### TimeLib_TickServer() Begins

The core server tick function is called by BYOND's time library. This process is single-threaded.

### Tick Operations (In Order)
1. **Time Update**
   + world.time increases by world.tick_lag milliseconds.
   + Internal time tracking is updated.

2. **TickProc() Execution**
   + Runs background procs (i.e. procs with set background=1).
   + Clears finished server-side animation records.
   + Processes sleeping/spawned scheduled procs.
   + Checks for thread-scheduled tasks from BYONDapi.
 
3. **Verbs**
   + Enqueued verbs are processed.
   + At this time, verb queueing is bypassed, so verbs occur between ticks, not during TimeLib_TickServer() calls.
 
4. **System Tasks**
   + Performs unique cell ID garbage collection.
   + Executes external system callbacks (Steamapi, etc.)
   + Processes additional thread callbacks.

5. **SendMaps()**
   + Performs sequential (non-threaded) client processing.
   + Spawns worker threads for parallel client processing.
   + Waits for all worker threads to complete.
   + Performs sequential (non-threaded) cleanup tasks.
 
6. **Final Tasks**
   + Processes remaining thread callbacks.
   + Prunes unneeded .rsc file batches.
   + Cleans temporary BYONDapi references.
   + Adjusts timing for the next tick.

### TimeLib_TickServer() Ends

However, this is still considered the same tick until the next time TimeLib_TickServer() is called for the purposes of any verbs called after the tick has completed.

### Between Ticks
Until the next TimeLib_TickServer() call:
  + Network traffic processing occurs.
  + Client verbs are received and executed.
  + Local Dream Seeker connections are handled.

### Next Tick Begins

The cycle repeats when TimeLib_TickServer() is called again.

> [!TIP]
> **See Also:**
> - [tick_lag var (world)](/ref/world/var/tick_lag.md)
> - [animate proc](/ref/proc/animate.md)
> - [background setting (proc)](/ref/proc/set_background.md)
> - [Understanding the Renderer](ref/notes/rendering/overview.md)
> - [Garbage Collection](/ref/DM/garbage.md)
> - [BYONDapi](/ref/appendix/Byondapi.md)
> - [GetAPI proc (client)](/ref/client/proc/GetAPI.md)
