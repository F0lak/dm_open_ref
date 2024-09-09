[]{#/callee}    
## callee {#callee byondver="516"}    
**See also:**    
:   [proc](/ref/proc)    
:   [vars (proc)](/ref/proc/var)    
:   [callee var (proc)](/ref/proc/var/callee)    
:   [caller var (proc)](/ref/proc/var/caller)    
:   [Error proc (world)](/ref/world/proc/Error)    
:   [try and catch statements](/ref/proc/try)    
A primitive type representing a running or sleeping proc. This gives    
access to the proc\'s information, and can be used to output a stack    
trace in situations such as writing your own custom `world.Error()`    
handler.    
You can get a `/callee` for the current running proc with its    
[callee](/ref/proc/var/callee){.code} var, or its caller with the    
[caller](/ref/proc/var/caller){.code} var. You can follow callers up the    
call chain.    
### Example:    
world/Error(err) world.log \<\< \"Error \[err\]:\" for(var/callee/p =    
caller, p, p = p.caller) world.log \<\< \" \[p.proc.type\]    
(src=\[p.src\], usr=\[p.usr\])\" if(p.file) world.log \<\< \" at    
\[p.file\]:\[p.line\]\"    
Built-in callee vars (read-only):    
[args](/ref/proc/var/args)    
[caller](/ref/proc/var/caller)    
[category](/ref/verb/set/category)[^\*^]{.small}    
[desc](/ref/verb/set/desc)[^\*^]{.small}    
file    
[name](/ref/verb/set/name)[^\*^]{.small}    
line    
proc    
[src](/ref/proc/var/src)    
type    
[usr](/ref/proc/var/usr)    
[^\*^ These vars are quick aliases for `proc.`*`varname`*. `proc.type`    
is excluded since `/callee` has its own type var.]{.small}    
The `file` and `line` vars are available if debugging information was    
turned on when the world was compiled. The other vars are all aliases    
for info about the running/sleeping proc or its prototype.    
Even though the `args` var itself is read-only, the list it returns is    
mutable. Making changes to the list will affect the proc it belongs to.  