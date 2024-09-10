[]{#/DOT proc.md}    
## . proc    
**See also:**    
:   [.. proc](/proc/%2e%2e)    
<!-- -->    
**Format:**    
:   .(Args)    
<!-- -->    
**Returns:**    
:   The return value of the current proc.    
<!-- -->    
**Args:**    
:   The arguments to pass to the new invocation of the current proc.    
    This defaults to current arguments.    
Call the current proc. A proc that calls itself is said to be recursive.    
### Example:    
proc/factorial(N as num) if(N\<=0) return 1 return .(N-1)\*N    
This computes the factorial N! by calling itself recursively.  