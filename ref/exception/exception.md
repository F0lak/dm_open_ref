[]{#/exception.md}    
## exception.md {#exception.md byondver="508"}    
**See also:**    
:   [try and catch statements](/proc/try)    
:   [Error proc (world)](/world/proc/Error)    
:   [throw statement](/proc/throw)    
:   [EXCEPTION proc](/proc/EXCEPTION)    
:   [caller var (proc)](/proc/var/caller)    
:   [stddef.dm file](/%7B%7Bappendix%7D%7D/stddef%2edm)    
<!-- -->    
**Vars:**    
:   name: A text string (such as an error message) or other value    
:   file: The filename where the error occurred, if debugging info is    
    present    
:   line: The line where the error occurred, if debugging info is    
    present    
:   desc: Detailed error info including call stack, only used when sent    
    to world.Error()    
This datum is created automatically when a runtime error is encountered,    
**if** it happens within a try/catch block or you have defined a global    
error handler with `world.Error()`. (The New() proc is not called when    
this happens.) This provides a convenient package for getting file and    
line number info associated with an error.    
If you throw your own exception.mds, you do not have to use this, but the    
`EXCEPTION` macro is provided to easily create one with the current file    
and line number.    
The `desc` value is only filled in when you have a world.Error() handler    
and there is no try/catch handling this error. Just like when no handler    
is present, less detail will be provided after multiple runtime errors    
have occurred. This only exists as a convenience feature for logging    
errors if you want to use something other than world.log.  