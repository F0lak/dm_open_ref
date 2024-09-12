## Entered proc (atom)

**Format:**
+   Entered(atom/movable/Obj,atom/OldLoc)
<!-- -->
**When:**
+   Called when an object has entered the contents list through Move().
    Directly setting the object\'s loc or step_x/y vars does not result
    in a call to Entered() or any other movement side-effects. The same
    goes for creation or deletion of an object at a location.
<!-- -->
**Args:**
+   Obj: the object that entered (a mob or obj).
+   OldLoc: the previous location of the object.
<!-- -->
**Default action:**
+   None for most atoms, but turfs will call Crossed().
### Example:

```
 turf/pit Entered(O) O \<\< \"OUCH. You fell in a pit!\"

```
 

The mob\'s Entered() and Exited() procs can be used
to control what happens when objects are added or removed from the
mob\'s inventory. Of course that could all be done within get() and
drop() verbs, but the following code separates user interface from
lower-level functions.
### Example:

```
 obj var weight = 10 verb get() set src in oview(1)
if(Move(usr)) usr \<\< \"You pick up \\a \[src\].\" else usr \<\< \"You
cannot pick up \[src\].\" drop() set src in usr if(Move(usr.loc)) usr
\<\< \"You drop \\a \[src\].\" mob var weight max_weight = 50
Entered(obj/O) weight += O.weight Exited(obj/O) weight -= O.weight
Enter(obj/O) //only allow entrance if weight is within the limit
if(O.weight + weight \<= max_weight) return ..() 
```
 

To
see the advantages of this arrangement, imagine that there are certain
situations in which an object may be created directly within the mob\'s
inventory without the mob picking it up. You can still run it through
your normal movement rules without calling get().
### Example:

```
 mob/verb/wish() var/obj/O = new() //create it with loc=null
if(O.Move(usr)) //and then move it into inventory usr \<\< \"Your wish
has been granted!\" else usr \<\< \"You are too greedy!\" del O

```


> [!TIP] 
> **See also:**
> +   [Enter proc (atom)](/ref/atom/proc/Enter.md) 
> +   [Exit proc (atom)](/ref/atom/proc/Exit.md) 
> +   [Exited proc (atom)](/ref/atom/proc/Exited.md) 
> +   [Cross proc (atom)](/ref/atom/proc/Cross.md) 
> +   [Crossed proc (atom)](/ref/atom/proc/Crossed.md) 
> +   [Uncross proc (atom)](/ref/atom/proc/Uncross.md) 
> +   [Uncrossed proc (atom)](/ref/atom/proc/Uncrossed.md) 
> +   [Move proc (movable atom)](/ref/atom/movable/proc/Move.md) 
> +   [step_x var (movable atom)](/ref/atom/movable/var/step_x.md) 
> +   [step_y var (movable atom)](/ref/atom/movable/var/step_y.md) <!-- -->