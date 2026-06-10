
## Crossed (proc)

**Format:**
+   Crossed(atom/movable/O)

**Arguments:**
+   O: the object that moved and is now overlapping.

**Called When:**
+   Called when an object has overlapped this one through Move(). Directly
setting the object's loc or step_x/y vars does not result in a call to
Crossed() or any other movement side-effects.  The same goes for creation
or deletion of an object at a location.

**Default Action:**
+   none
***

```dm

obj/landmine
   Crossed(O)
      O << "You stepped on a land mine!"
      Explode()

```

***
**Related Pages:**
+    [Enter proc (atom)](/ref/atom/proc/Enter)
+    [Entered](/ref/atom/proc/Entered)
+    [Exit proc (atom)](/ref/atom/proc/Exit)
+    [Exited](/ref/atom/proc/Exited)
+    [Cross proc (atom)](/ref/atom/proc/Cross)
+    [Uncross proc (atom)](/ref/atom/proc/Uncross)
+    [Uncrossed proc (atom)](/ref/atom/proc/Uncrossed)
+    [Move proc (movable atom)](/ref/atom/movable/proc/Move)
+    [group](/ref/mob/var/group)
+    [Pixel movement](/ref/{notes}/pixel-movement)
