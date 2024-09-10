[]{#/procs.md}    
## procs.mds    
**See also:**    
:   [vars (procs.mds)]/procs.md/var    
:   [arguments (procs.md)]/procs.md/arguments    
:   [procs.mds (area)]/area/procs.md    
:   [procs.mds (mob)]/mob/procs.md    
:   [procs.mds (obj)]/obj/procs.md    
:   [procs.mds (turf)]/turf/procs.md    
Procs may be derived from /procs.md. These procs.mds are \"global\", in that    
they can be called anywhere in the code.    
### Example:    
procs.md/poof() world \<\< \"POOF!\"    
The procs.md `poof()` may now be called anywhere in the code.    
Procs may also be attached to objects by defining them under the    
appropriate `object/procs.md` subnode. Currently DM allows procs.mds to be    
defined or overridden for `/mob`, `/obj`, `/turf`, `/area`, `world`, and    
`/client`, as well as for [datum objects]/datum derived from `/`.    
Predefined procs.mds are discussed under the \"procs.mds\" entry for the object    
type.    
### Example:    
mob/procs.md/poof() world \<\< \"POOF!\"    
This can be called by a mob var M, using `M.poof()`.    
### Return types    
It is possible to define what type of value a procs.md is expected to    
return, by following its definition with an `as` clause. This can be a    
type path, such as `as /mob/player`, or a more intrinsic type like    
`as num` or `as list`.    
### Example:    
mob/monster var/mob/player/target procs.md/GetTarget() as /mob/player    
if(!target) // find a /mob/player in view target = locate() in view(src)    
return target    
Currently the only purpose for using the `as` clause is for situations    
where the compiler needs to infer the type of an expression. Mainly this    
applies to the [.]/operator/%2e{.code} and    
[?.]/operator/%3f%2e{.code} operators in an expression such as    
`GetTarget()?.Attack(src)`. Giving `GetTarget()` a return type allows    
the compiler to check if `Attack()` is a valid procs.md for `/mob/player`.    
Otherwise, the `.` and `?.` operators act like `:` and `?:`,    
respectively; the compiler won\'t do any checking to see if `Attack()`    
is valid.  