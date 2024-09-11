## vars list var (datum)
**See also:**
*   [initial proc](/ref/proc/initial.md) -m
*   [issaved proc](/ref/proc/issaved.md) -m
*   [list](/ref/list.md) -m
*   [list associations](/ref/list/associations.md) -m
*   [vars list var (global)](/ref/DM/vars.md) -m

This is a list of all the variables belonging to an object. The
items in the list are the variable names. If the variable name is used
as an index into the list, the value of that variable is accessed.
### Example:

```
 mob/verb/dump() var/V for(V in vars) usr \<\< \"\[V\] =
\[vars\[V\]\]\" 
```
 

This example displays all the
variables belonging to your mob.