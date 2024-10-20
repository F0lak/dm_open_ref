## SIDE_MAP Topological Sorting

The topological sort for SIDE_MAP is determined in the following order:

-	If two icons don't overlap visually, they don't care about their relative order.
-	If one icon is physically completely in front of the other, draw it later.
-	If one has a higher layer, draw it later.
-	If one's physical near-Y (edge toward the bottom of the screen) is nearer, draw it later.
-	If both icons have the exact same physical bounds, use their original order to determine which draws first.
-	If one icon's virual center X is further left, draw it first.
-	Break all remaining ties with the original order.

> [!NOTE]
> The first condition that is met determines the drawing order

> [!TIP]
> **See Also:**
> - [Understanding the Rendereer](ref/notes/rendering/overview.md)
> - [map_format var (world)](/ref/world/var/map_format.md)