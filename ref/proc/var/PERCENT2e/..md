[]{#/proc/var/%2e toc="."}    
## . var (proc)    
**See also:**    
:   [return statement](/ref/proc/return.md)    
:   [vars (procs)](/ref/proc/var.md)    
This is the default return value. If a proc exits without calling return    
or if no arguments are specified the value of `.` will be returned. The    
default value of `.` is null.    
### Example:    
mob/Login() . = ..() view() \<\< \"\[src\] logs in.\"  