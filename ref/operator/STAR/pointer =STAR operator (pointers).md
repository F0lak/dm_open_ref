## \* pointer operator 
###### BYOND Version 515

**Format:**
+   \*A
<!-- -->
**Returns:**
+   The value pointed at by a pointer stored in A
This operator is also called the dereference operator, since it takes a
pointer reference and gives you the value within.) 

When using
the `&` operator to get a reference pointer, you can access the value it
points to with this version of the `*` operator. This can also be used
on the left-hand side of assignment operations, for instance `*A = B` or
`*X += Y`, to store the result in the place the pointer indicates.
### Example:

``` dm
 atom/proc/PixelPos(px, py) // get an exact step position
\*px = (x-1) \* 32 // this code assumes a 32x32 icon size \*py = (y-1)
\* 32 atom/movable/PixelPos(px, py) // get an exact step position ..()
\*px += step_x // this code assumes a 32x32 icon size \*py += step_y
mob/verb/WhereAmI() var/X, Y PixelPos(&X, &Y) usr \<\< \"You are at
\[X\],\[Y\] on level \[z\]\" 
```
 

Note: If you try to
read to or write from a pointer reference that is no longer valid, such
as to a var inside a proc that has ended, the read or write will fail
silently; reading will return a null value. (An exception is pointers to
list items. If the index is out of bounds, you will get the expected
error.)

> [!TIP] 
> **See also:**
> +   [& pointer operator](/ref/operator/&/pointer.md) 
> +   [operators](/ref/operator.md) 
> +   [ispointer proc](/ref/proc/ispointer.md) <!-- -->