## get_dir proc

**Format:**
+   get_dir(Loc1, Loc2)

**Returns:**
+   The direction from Loc1 to Loc2.

**Args:**
+   Loc1: An object on the map.
+   Loc2: An object on the map.

If `Loc1` and `Loc2` are the same, this will return `0`. Otherwise, possible results are `NORTH`,
`SOUTH`, `EAST`, `WEST`, `NORTHEAST`, `NORTHWEST`, `SOUTHEAST`, and
`SOUTHWEST`.

If the direction is not directly lying along one of the four
primary cardinal directions, the result will become the nearest diagonal
direction (eg. if `Loc2` is mostly north but a little to the east of
`Loc1`, the direction returned will be `NORTHEAST`).

> [!TIP] 
> **See also:**
> +   [dir var (atom)](/ref/atom/var/dir.md) 
