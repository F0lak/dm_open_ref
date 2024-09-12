## get_dir proc
**See also:**
+   [dir var (atom)](/ref/atom/var/dir.md) <!-- -->
**Format:**
+   get_dir(Loc1, Loc2)
<!-- -->
**Returns:**
+   The direction from Loc1 to Loc2. Possible results are `NORTH`,
    `SOUTH`, `EAST`, `WEST`, `NORTHEAST`, `NORTHWEST`, `SOUTHEAST`, and
    `SOUTHWEST`.
<!-- -->
**Args:**
+   Loc1: An object on the map.
+   Loc2: An object on the map.


If the direction is not directly lying along one of the four
primary cardinal directions, the result will become the nearest diagonal
direction (eg. if `Loc2` is mostly north but a little to the east of
`Loc1`, the direction returned will be `NORTHEAST`).