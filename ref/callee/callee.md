## callee 
###### BYOND Version 516
**See also:**
*   [proc](/proc)
*   [vars (proc)](/proc/var)
*   [callee var (proc)](/proc/var/callee)
*   [caller var (proc)](/proc/var/caller)
*   [Error proc (world)](/world/proc/Error)
*   [try and catch statements](/proc/try)


A primitive type representing a running or sleeping proc. This
gives access to the proc\'s information, and can be used to output a
stack trace in situations such as writing your own custom
`world.Error()` handler. 

You can get a `/callee` for the
current running proc with its [`callee`](/proc/var/callee) var, or
its caller with the [`caller`](/proc/var/caller) var. You can
follow callers up the call chain.
### Example:

```
 world/Error(err) world.log \<\< \"Error \[err\]:\"
for(var/callee/p = caller, p, p = p.caller) world.log \<\< \"
\[p.proc.type\] (src=\[p.src\], usr=\[p.usr\])\" if(p.file) world.log
\<\< \" at \[p.file\]:\[p.line\]\" 
```
 

Built-in callee
vars (read-only):
[args](/proc/var/args)
[caller](/proc/var/caller)
[category](/verb/set/category)[^\*^]{.small}
[desc](/verb/set/desc)[^\*^]{.small}
file
[name](/verb/set/name)[^\*^]{.small}
line
proc
[src](/proc/var/src)
type
[usr](/proc/var/usr)


[^\*^ These vars are quick aliases for `proc.`*`varname`*.
`proc.type` is excluded since `/callee` has its own type var.]{.small}


The `file` and `line` vars are available if debugging
information was turned on when the world was compiled. The other vars
are all aliases for info about the running/sleeping proc or its
prototype. 

Even though the `args` var itself is read-only, the
list it returns is mutable. Making changes to the list will affect the
proc it belongs to.