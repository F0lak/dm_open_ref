## nameof proc 
###### BYOND Version 515

**Format:**
+   nameof(Var)
+   nameof(ProcRef)
+   nameof(Path)
<!-- -->
**Args:**
+   Var: A variable, e.g. src.density or foo::bar.
+   ProcRef: A proc reference, e.g. /mob::Enter().
+   Path: A type path, e.g. /obj/item/barrel.


This returns the name of a var or proc, or the last part of a
type path. This proc only exists at compile-time. 

The main
purpose of this proc is to turn a proc reference into a name, which is
useful in some esoteric situations.
### Example:

```dm
 var/list/event_queue proc/CallLater(object, procref, a, b,
c) var/list/forlater = list(object, nameof(procref), a, b, c)
event_queue \|\|= list() event_queue[++event_queue.len] = forlater
world/Tick() while(length(event_queue)) var/list/forlater =
event_queue[1] event_queue.Cut(1,2) var/object = forlater[1]
var/procname = forlater[2] var/a = forlater[3] var/b = forlater[4]
var/c = forlater[5] call(object, procname)(a, b, c) 
```


> [!TIP] 
> **See also:**
> +   [:: operator](/ref/operator/::.md) <!-- -->