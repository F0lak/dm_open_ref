[]{#/proc/var/caller}    
## caller var (proc) {#caller-var-proc byondver="516"}    
**See also:**    
:   [callee](ref/callee)    
:   [callee var (proc)](ref/proc/var/callee)    
Returns a [callee object](ref/callee) representing the current proc\'s    
caller, which can be used to access information like the proc name, line    
number (if compiled with debug information), arguments, and more.    
The main purpose of this is to make it possible to trace the call stack    
when handling errors.    
### Example:    
world/Error(err) world.log \<\< \"Error \[err\]:\" for(var/callee/p =    
caller, p, p = p.caller) world.log \<\< \" \[p.type\] (src=\[p.src\],    
usr=\[p.usr\])\" if(p.file) world.log \<\< \" at \[p.file\]:\[p.line\]\"  