
## callee (info)
***
A primitive type representing a running or sleeping proc. This gives access to the proc's information, and can be used to output a stack trace in situations such as writing your own custom `world.Error()` handler.

You can get a `/callee` for the current running proc with its <a class="code" href="#/proc/var/callee">callee</a> var, or its caller with the <a class="code" href="#/proc/var/caller">caller</a> var. You can follow callers up the call chain.


```dm

world/Error(err)
    world.log << "Error [err]:"
    for(var/callee/p = caller, p, p = p.caller)
        world.log << "  [p.proc.type] (src=[p.src], usr=[p.usr])"
        if(p.file) world.log << "    at [p.file]:[p.line]"

```


Built-in callee vars (read-only):

<small><sup>*</sup> These vars are quick aliases for `proc.*varname*`. `proc.type` is excluded since `/callee` has its own type var.</small>

The `file` and `line` vars are available if debugging information was turned on when the world was compiled. The other vars are all aliases for info about the running/sleeping proc or its prototype.

Even though the `args` var itself is read-only, the list it returns is mutable. Making changes to the list will affect the proc it belongs to.
***
**Related Pages:**
+    [procs](/ref/proc)
+    [vars (procs)](/ref/proc/var)
+    [callee var (proc)](/ref/proc/var/callee)
+    [caller var (proc)](/ref/proc/var/caller)
+    [Error proc (world)](/ref/world/proc/Error)
+    [try and catch statements](/ref/proc/try)
