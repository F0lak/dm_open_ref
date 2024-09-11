## procs
**See also:**
*   [vars (procs)](/proc/var)
*   [arguments (proc)](/proc/arguments)
*   [procs (area)](/area/proc)
*   [procs (mob)](/mob/proc)
*   [procs (obj)](/obj/proc)
*   [procs (turf)](/turf/proc)


Procs may be derived from /proc. These procs are \"global\", in
that they can be called anywhere in the code.
### Example:

```
 proc/poof() world \<\< \"POOF!\" 
```
 

The proc
`poof()` may now be called anywhere in the code. 

Procs may also
be attached to objects by defining them under the appropriate
`object/proc` subnode. Currently DM allows procs to be defined or
overridden for `/mob`, `/obj`, `/turf`, `/area`, `world`, and `/client`,
as well as for [datum objects](/datum) derived from `/`. Predefined
procs are discussed under the \"procs\" entry for the object type.
### Example:

```
 mob/proc/poof() world \<\< \"POOF!\" 
```
 

This
can be called by a mob var M, using `M.poof()`.
### Return types


It is possible to define what type of value a proc is expected
to return, by following its definition with an `as` clause. This can be
a type path, such as `as /mob/player`, or a more intrinsic type like
`as num` or `as list`.
### Example:

```
 mob/monster var/mob/player/target proc/GetTarget() as
/mob/player if(!target) // find a /mob/player in view target = locate()
in view(src) return target 
```
 

Currently the only
purpose for using the `as` clause is for situations where the compiler
needs to infer the type of an expression. Mainly this applies to the
[`.`](/operator/%2e) and [`?.`](/operator/%3f%2e) operators
in an expression such as `GetTarget()?.Attack(src)`. Giving
`GetTarget()` a return type allows the compiler to check if `Attack()`
is a valid proc for `/mob/player`. Otherwise, the `.` and `?.` operators
act like `:` and `?:`, respectively; the compiler won\'t do any checking
to see if `Attack()` is valid.