[]{#/callee}    
## callee {#callee byondver="516"}    
**See also:**    
:   [proc](/ref/proc/proc.md)    
:   [vars (proc)](/ref/proc/var/var.md)    
:   [callee var (proc)](/ref/proc/var/callee/callee.md)    
:   [caller var (proc)](/ref/proc/var/caller/caller.md)    
:   [Error proc (world)](/ref/world/proc/Error/Error.md)    
:   [try and catch statements](/ref/proc/try/try.md)    
A primitive type representing a running or sleeping proc. This gives    
access to the proc\'s information, and can be used to output a stack    
trace in situations such as writing your own custom `world.Error()`    
handler.    
You can get a `/callee` for the current running proc with its    
[callee](/ref/proc/var/callee/callee.md){.code} var, or its caller with the    
[caller](/ref/proc/var/caller/caller.md){.code} var. You can follow callers up the    
call chain.    
### Example:    
world/Error(err) world.log \<\< \"Error \[err\]:\" for(var/callee/p =    
caller, p, p = p.caller) world.log \<\< \" \[p.proc.type\]    
(src=\[p.src\], usr=\[p.usr\])\" if(p.file) world.log \<\< \" at    
\[p.file\]:\[p.line\]\"    
Built-in callee vars (read-only):    
[args](/ref/proc/var/args/args.md)    
[caller](/ref/proc/var/caller/caller.md)    
[category](/ref/verb/set/category/category.md)[^\*^]{.small}    
[desc](/ref/verb/set/desc/desc.md)[^\*^]{.small}    
file    
[name](/ref/verb/set/name/name.md)[^\*^]{.small}    
line    
proc    
[src](/ref/proc/var/src/src.md)    
type    
[usr](/ref/proc/var/usr/usr.md)    
[^\*^ These vars are quick aliases for `proc.`*`varname`*. `proc.type`    
is excluded since `/callee` has its own type var.]{.small}    
The `file` and `line` vars are available if debugging information was    
turned on when the world was compiled. The other vars are all aliases    
for info about the running/sleeping proc or its prototype.    
Even though the `args` var itself is read-only, the list it returns is    
mutable. Making changes to the list will affect the proc it belongs to.  