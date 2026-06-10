
## Cross (proc)

**Format:**
+   Cross(atom/movable/O)

**Arguments:**
+   O: the object attempting to overlap.

**Returns:**
+   1 to permit; 0 to deny.

**Called When:**
+   Called when another object attempts to overlap this one.

**Default Action:**
+   Allow overlap unless both atoms are dense. If both atoms are mobs, the
behavior depends partly on whether they are in the same group.
***

> [!NOTE]
> The following behavior only applies to <a class="code" href="#/world/var/movement_mode">LEGACY_MOVEMENT_MODE</a>. In other movement modes, src.Cross(O) returns 0 by default if src and O are both mobs in the same group.

If src completely covers the turf it is standing on, Cross() is called as part of turf.Enter(). This is to preserve the behavior of older games, which expect turf.Enter() to care about its contents.

If src and O are both mobs, and O is in src's group, overlap is allowed *unless* neither of them use pixel movement. Older games that do not use pixel movement expect that Bump() will be called, and by default Bump() will swap the mobs' positions. Swapping obviously only works in situations where a mob takes up a whole tile and only moves by tiles; for all other situations, allowing an overlap makes more sense.
***
**Related Pages:**
+    [Enter proc (atom)](/ref/atom/proc/Enter)
+    [Entered](/ref/atom/proc/Entered)
+    [Exit proc (atom)](/ref/atom/proc/Exit)
+    [Exited](/ref/atom/proc/Exited)
+    [Crossed proc (atom)](/ref/atom/proc/Crossed)
+    [Uncross proc (atom)](/ref/atom/proc/Uncross)
+    [Uncrossed proc (atom)](/ref/atom/proc/Uncrossed)
+    [Move proc (movable atom)](/ref/atom/movable/proc/Move)
+    [group](/ref/mob/var/group)
+    [movement_mode var (world)](/ref/world/var/movement_mode)
+    [Pixel movement](/ref/{notes}/pixel-movement)
