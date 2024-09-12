## lazy_eye var (client)
**See also:**
+   [view var (client)](/ref/client/var/view.md) 
+   [view var (world)](/ref/world/var/view.md) <!-- -->
**Default value:**
+   0


This is the maximum \"lag\" between client.eye and client.mob.
The mob can stray up to this many tiles before the eye will move to keep
it in view. The default value of 0 means that the eye always moves as
the mob moves, keeping the mob at the center of the player\'s map.


Setting this value to a non-zero value automatically
initializes client.eye to client.mob.loc (or to the center of the full
map if that is possible). Thereafter, client.eye will stray from the mob
as it moves about the map, making one big jump to catch up whenever the
mob gets out of range.
### Example:

```
 client lazy_eye = 5 
```
 

This setting allows
client.mob to move onto the entire 11x11 visible region without changing
the value of client.eye. The moment it steps out of this region, the
entire region will shift 5 tiles in the direction of motion.


You can assign lazy_eye to any value valid as a view size, so,
for example, if you have a non-square setting for client.view, say,
\"17x11\", you could apply a similar setting to lazy_eye. You can even
make one dimension lazy and the other one strictly centered+ \"0x5\".