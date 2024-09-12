## bounds var (client) 
###### BYOND Version 509
(Also `bound_x`, `bound_y`, `bound_width`, and `bound_height`.)
**See also:**
*   [bounds proc](/ref/proc/bounds.md) 

The read-only bounds var returns the map coordinates, in
pixels, covered by the client\'s viewport when accounting for pixel
offsets, eye, step, etc. (The coordinates are only relevant to the
default `client.dir` value of `NORTH`, and the `TOPDOWN_MAP` or
`SIDE_MAP` map formats.) 

If the viewport is not currently on
the map (for instance, when the eye is at a null location), the var
reads as null. Otherwise, it is a list with five values (x, y, width,
height, z) in the same form used by the bounds proc. 

The alias
vars bound_x, bound_y, bound_width, and bound_height can also be used to
retrieve the individual values from the list. They too will be null if
the viewport is not on the map.