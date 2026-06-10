
## caller (var)
***
Returns a <a href="#/callee">callee object</a> representing the current proc's caller, which can be used to access information like the proc name, line number (if compiled with debug information), arguments, and more.

The main purpose of this is to make it possible to trace the call stack when handling errors.


```dm

world/Error(err)
    world.log << "Error [err]:"
    for(var/callee/p = caller, p, p = p.caller)
        world.log << "  [p.type] (src=[p.src], usr=[p.usr])"
        if(p.file) world.log << "    at [p.file]:[p.line]"

```

***
**Related Pages:**
+    [callee](/ref/callee)
+    [callee var (proc)](/ref/proc/var/callee)
