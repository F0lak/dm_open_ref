
## x (var)

**Default Value:**
+   The x coordinate of the object on the map.
***
You may assign the coordinates of movable objects (mobs and objs), but this is not advisable. It is better to compute the new location (with <code>locate()</code>) and move them to that. Then you can use the normal <code>Move()</code> procedure, which enables all the normal movement behavior.

For areas that are on the map, this is the coordinate of the turf with the lowest z, y, and x coordinate (in that order) that is contained by the area.
***
**Related Pages:**
+    [loc](/ref/atom/var/loc)
