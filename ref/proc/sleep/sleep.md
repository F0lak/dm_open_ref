[]{#/proc/sleep}    
## sleep proc    
**See also:**    
:   [background setting (proc)](/ref/proc/set/background.md)    
:   [waitfor setting (proc)](/ref/proc/set/waitfor.md)    
:   [spawn proc](/ref/proc/spawn.md)    
:   [tick_lag var (world)](/ref/world/var/tick_lag.md)    
<!-- -->    
**Format:**    
:   sleep(Delay)    
<!-- -->    
**Args:**    
:   Delay: The amount of time to sleep, in 1/10 seconds.    
::: {.sidebar .underhood}    
When a proc sleeps, it actually makes a copy of itself. The copy is what    
will wake up later, and the current proc simply ends. The same thing    
happens to its callers.    
:::    
Pause the current proc (and its callers) for a specified amount of time.    
If no delay is specified, it will be scheduled to resume as soon as    
other immediately pending events are processed.    
Note that sleeping in some procedures results in the return value being    
lost. For example, if you sleep inside `Entered()` or `Exited()`, it    
will be as if you returned immediately where you started sleeping. This    
is because `Move()` calls them in away that says the return value should    
be ignored. Also if a proc has its [waitfor](/ref/proc/set/waitfor.md){.code}    
setting changed to 0, it will return the value of the `.` var to its    
caller immediately if it or one of its callees sleeps.    
Also be aware that a sleeping procedure whose `src`{.variable} object    
gets deleted will automatically terminate when execution returns to it.    
This is to protect you against trying to access properties or procedures    
of a deleted (and therefore `null`) object. If you do not want the    
procedure to be terminated, you should set `src`{.variable} to `null`.    
One common use of `sleep` is to create what is known as a *ticker*. That    
is an infinite loop that performs some periodic operation.    
### Example:    
proc/Weather() spawn while(1) //infinite ticker loop world \<\< \"The    
sun rises in the east.\" sleep(500) world \<\< \"The noon day sun rises    
high in the sky.\" sleep(500) world \<\< \"The sun sinks low in the    
west.\" sleep(1000)    
Notice how such infinite loops are usually created using `spawn` to    
prevent the caller from getting locked up. You could call this procedure    
from `world.New()` to start it rolling.    
Note: sleep time is in 1/10s units, not server ticks. If your    
`world.tick_lag` or `world.fps` value is different from the default,    
`sleep(1)` still means \"sleep for 1/10s\". To sleep for exactly `N`    
ticks, call `sleep(N * world.tick_lag)`.    
If the ticker does intensive processing during each iteration, you    
probably want to run it in the background like this: proc/Ticker() set    
background = 1    
Calling sleep() with a negative argument (such as sleep(-1)) causes it    
to do a backlog check. Only if other pending events have become    
backlogged will it sleep. This is similar to running in the background,    
but you manually control where the backlog checks are made. The    
difference between this and sleep(0) is that sleep(0) *always* sleeps    
the current procedure for as short a time as possible, whereas sleep(-1)    
only sleeps the current procedure if other scheduled events have become    
backlogged. Therefore, sleep(-1) will tend to run the current procedure    
at a higher priority with fewer interruptions. It is appropriate when    
there is a single task that needs to be done before anything else can    
happen, and you just want to make sure that network and user I/O are not    
terribly lagged in the process.  