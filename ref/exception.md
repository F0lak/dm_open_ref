
## exception (info)
***
This datum is created automatically when a runtime error is encountered, **if** it happens within a try/catch block or you have defined a global error handler with `world.Error()`. (The New() proc is not called when this happens.) This provides a convenient package for getting file and line number info associated with an error.

If you throw your own exceptions, you do not have to use this, but the `EXCEPTION` macro is provided to easily create one with the current file and line number.

The `desc` value is only filled in when you have a world.Error() handler and there is no try/catch handling this error. Just like when no handler is present, less detail will be provided after multiple runtime errors have occurred. This only exists as a convenience feature for logging errors if you want to use something other than world.log.
***
**Related Pages:**
+    [try and catch statements](/ref/proc/try)
+    [Error proc (world)](/ref/world/proc/Error)
+    [throw statement](/ref/proc/throw)
+    [EXCEPTION proc](/ref/proc/EXCEPTION)
+    [caller var (proc)](/ref/proc/var/caller)
+    [stddef.dm file](/ref/{{appendix}}/stddef%2edm)
