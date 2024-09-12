## pixloc proc 
###### BYOND Version 516
**See also:**
*   [pixloc](/ref/pixloc.md) 
*   [pixloc var (atom)](/ref/atom/var/pixloc.md) 
*   [bound_pixloc proc](/ref/proc/bound_pixloc.md) <!-- -->
**Format:**
*   pixloc(x, y, z)
*   pixloc(Atom)
*   pixloc(Atom, x, y)
*   pixloc(Atom, Vector)
*   pixloc(Pixloc)
*   pixloc(Pixloc, x, y)
*   pixloc(Pixloc, Vector)
<!-- -->
**Returns:**
*   A new `pixloc` object or null.
<!-- -->
**Args:**
*   x, y, z* Pixel coordinates in world space (starting at 1,1,1). When
    the first argument is an atom or pixloc, x and y are offsets.
*   Atom* An atom whose pixloc will be copied.
*   Pixloc* An existing pixloc to copy.
*   Vector* A 2D vector to offset the new pixloc by.


Creates a new `pixloc` object based on an existing object\'s
location or using raw world coordinates. If the pixloc can\'t be
created, for instance if the Atom argument is not directly on the map,
the result is null.
### Example:

```
 mob/proc/GoToStrangeForest() // in a world with 32x32 icon
size, this is x=18, y=29, step_x=5, step_y=11 mob.pixloc = pixloc(550,
907, 1) 
```
 

When the pixloc is created with world
coordinates, x and y are a combination of tile x and step_x, and tile y
and step_y, starting at a value of 1. The world x and y for any tile and
step combo can be calculated like so (if for any reason you needed to):

```
 world_x = (tile_x - 1) \* pixels_per_x_tile + step_x + 1
world_y = (tile_y - 1) \* pixels_per_y_tile + step_y + 1 
```
