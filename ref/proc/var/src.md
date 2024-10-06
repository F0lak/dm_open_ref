## src var (proc)



This is a variable equal to the object containing the proc or
verb. It is defined to have the same type as that object.
### Example:

```dm
 obj/bread verb/eat() world << "[usr] eats [src]"

```
 

If a player named "Bob" calls "eat bread", the
output will be "Bob eats the bread." 

Note that `src` has no
meaning for global procs, derived from `/proc`, unless they are invoked
as verbs (by being attached to a [verb list](/ref/atom/var/verbs.md) .

> [!TIP] 
> **See also:**
> +   [usr var (proc)](/ref/proc/var/src.md) 
> +   [procs](/ref/proc.md) 
> +   [verbs](/ref/verb.md) 