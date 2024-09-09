[]{#/world/proc/Error}    
## Error proc (world) {#error-proc-world byondver="508"}    
**See also:**    
:   [try and catch statements](/ref/proc/try)    
:   [throw statement](/ref/proc/throw)    
:   [exception](/ref/exception)    
<!-- -->    
**Format:**    
:   Error(exception)    
<!-- -->    
**Args:**    
:   exception: The error that was thrown. If this was a runtime error,    
    the value will be an /exception datum.    
Called when a runtime error happens, or the throw keyword is used,    
without a try/catch to handle it. The return value is ignored.  