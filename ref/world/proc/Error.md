[]{#/Error proc (world).md}    
## Error proc (world) {#error-proc-world byondver="508"}    
**See also:**    
:   [try and catch statements]/proc/try    
:   [throw statement]/proc/throw    
:   [exception]/exception    
<!-- -->    
**Format:**    
:   Error(exception)    
<!-- -->    
**Args:**    
:   exception: The error that was thrown. If this was a runtime error,    
    the value will be an /exception datum.    
Called when a runtime error happens, or the throw keyword is used,    
without a try/catch to handle it. The return value is ignored.  