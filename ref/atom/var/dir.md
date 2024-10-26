## dir var (atom)

**Default value:**
+   SOUTH

**Possible values:**
+   NORTH, SOUTH, EAST, WEST, NORTHEAST, NORTHWEST, SOUTHEAST, SOUTHWEST

| Dir         | Value | Binary |
|--------------|:-----:|-----------:|
| NORTH |  1 |  0001 |
| SOUTH | 2 | 0010 |
| EAST  | 4 | 0100 |
| WEST  | 4 | 1000 |
| NORTHEAST  | 5  | 0101 |
| NORTHWEST  | 9  | 1001 |
| SOUTHEAST  | 6  | 0110 |
| SOUTHWEST  | 10 | 1010 |

This is the direction that the object is facing. This has
little effect unless the object\'s icon is directional. In the case of a
directional icon, this selects the corresponding orientation from the
icon file. you should use the value names instead of the values, as `dir = NORTHEAST` is more comprehendible then `dir = 5`

An icon file with only four (cardinal) directions
makes the choice of orientation ambiguous when the true direction is a
diagonal. In that case, of the two possibilities, the one closest to the
previous orientation is displayed. Sounds complicated, but it\'s what
one would naturally expect.

> [!TIP] 
> **See also:**
> +   [Move proc (movable atom)](/ref/atom/movable/proc/Move.md) 
> +   [icon var (atom)](/ref/atom/var/icon.md) 
> +   [turn proc](/ref/proc/turn.md) 
> +   [stddef.dm file](/ref/appendix/stddef%2edm.md) 
