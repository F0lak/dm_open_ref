
## Uncross (proc)

**Format:**
+   Uncross(atom/movable/O)

**Arguments:**
+   O: the object attempting to get away.

**Returns:**
+   1 to permit; 0 to deny.

**Called When:**
+   Called when another object attempts to stop overlapping this one.

**Default Action:**
+   Allow the object to get away (returning 1)
******
**Related Pages:**
+    [Enter proc (atom)](/ref/atom/proc/Enter)
+    [Entered](/ref/atom/proc/Entered)
+    [Exit proc (atom)](/ref/atom/proc/Exit)
+    [Exited](/ref/atom/proc/Exited)
+    [Cross proc (atom)](/ref/atom/proc/Cross)
+    [Crossed proc (atom)](/ref/atom/proc/Crossed)
+    [Uncrossed proc (atom)](/ref/atom/proc/Uncrossed)
+    [Move proc (movable atom)](/ref/atom/movable/proc/Move)
+    [group](/ref/mob/var/group)
+    [Pixel movement](/ref/{notes}/pixel-movement)
