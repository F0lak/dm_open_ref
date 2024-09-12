## tmp vars
**See also:**
+   [savefile](/ref/savefile.md) 
+   [vars](/ref/var.md) 


The tmp type modifier indicates that an object variable should
not be automatically written to the save file. This could mean that the
variable is transient---that is, it is calculated at run-time and need
not be saved. It could also indicated that the designer will handle
saving of that variable specially and wishes to bypass the automated
routine. 

It is especially important to use tmp when you have
references to external objects that should not be saved along with the
object. For example, suppose players have a `leader`{.variable} variable
which indicates who or what they are following. You would not
necessarily want the leader to be saved in the player\'s savefile.
Therefore, you would need to use `tmp` when defining the variable.
### Example:

```
 mob var/tmp leader verb follow(mob/M) leader = M 
```

::: {.sidebar .note}


Accidentally saving another mob in your savefile can be
disastrous. This can happen if you save a turf that the mob is standing
on, or if you save an obj with a non-tmp var that points to that mob,
and many other ways. 

The reason this is a problem is that
another player\'s mob will have the `key` var set already. When that mob
is loaded, if they are already logged into the game they will be
immediately reassigned to that just-loaded, older mob with a `Login()`
call, while the mob they\'re supposed to be using will have `Logout()`
called. Thus they\'ll appear to \"rollback\" to an earlier state.


If your game accidentally falls into this trap, don\'t panic!
You can look at your savefiles via
[ImportText()](/ref/savefile/ImportText.md) {.code} or in an editor to see
which var is the problem. Once you change that var to `/tmp`, you can
override [Read()](/ref/datum/proc/Read.md) {.code} so if that var is present,
you can remove it before calling `..()` to finish loading.
:::
The following built-in variables are defined as tmp vars:
+   [type](/ref/datum/var/type.md) 
+   [parent_type](/ref/datum/var/parent_type.md) 
+   [vars](/ref/datum/var/vars.md) 
+   [verbs](/ref/atom/var/verbs.md) 
+   [group](/ref/mob/var/group.md) 
+   [loc](/ref/atom/var/loc.md) 
+   [locs](/ref/atom/var/locs.md) 
+   [vis_locs](/ref/atom/var/vis_locs.md) 
+   [x](/ref/atom/var/x.md) 
+   [y](/ref/atom/var/y.md) 
+   [z](/ref/atom/var/z.md) 
+   [ckey](/ref/mob/var/ckey.md) 
+   [visibility](/ref/atom/var/visibility.md) 
+   [bound_x](/ref/atom/movable/var/bound_x.md) 
+   [bound_y](/ref/atom/movable/var/bound_y.md) 
+   [bound_width](/ref/atom/movable/var/bound_width.md) 
+   [bound_height](/ref/atom/movable/var/bound_height.md) 
+   [mouse_over_pointer](/ref/atom/var/mouse_over_pointer.md) 
+   [mouse_drag_pointer](/ref/atom/var/mouse_drag_pointer.md) 
+   [mouse_drop_pointer](/ref/atom/var/mouse_drop_pointer.md) 