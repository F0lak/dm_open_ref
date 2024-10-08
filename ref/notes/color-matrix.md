## Color matrix 
###### BYOND Version 509

A color matrix is used to transform colors, in the same way
that a matrix represented by the `/matrix` datum is used to transform 2D
coordinates. A transformation matrix is 3x3, of which only 6 values are
needed because the last column is always the same. A color matrix,
because it transforms four different numbers instead of two, is 5x5.
```
                    |rr rg rb ra 0|
                    |gr gg gb ga 0|
    [r g b a 255] x |br bg bb ba 0| = [r' g' b' a' 255]
                    |ar ag ab aa 0|
                    |cr cg cb ca 1|
```

In easier-to-understand terms, this is how the result is
calculated: 
```dm
new_red   = red * rr + green * gr + blue * br + alpha * ar + 255 * cr
new_green = red * rg + green * gg + blue * bg + alpha * ag + 255 * cg
new_blue  = red * rb + green * gb + blue * bb + alpha * ab + 255 * cb
new_alpha = red * ra + green * ga + blue * ba + alpha * aa + 255 * ca
```
 
It is helpful to think of each row in the matrix as what each component of the
original color will become. The first row of the matrix is the rgba
value you\'ll get for each unit of red; the second is what each green
becomes, and so on. 

Because the fifth column of the matrix is
always the same, only 20 of the values need to be provided. You can use
a color matrix with atom.color or client.color in any of the following
ways:
+ **RGB-only (9 to 12 values)**: `list(rr,rg,rb, gr,gg,gb, br,bg,bb, cr,cg,cb)`
+ **RGBA (16 to 20 values)**: `list(rr,rg,rb,ra, gr,gg,gb,ga, br,bg,bb,ba, ar,ag,ab,aa,
    cr,cg,cb,ca)`
+ **Row-by-row (3 to 5 `rgb()` values, or null to use the default row)**: `list(red_row, green_row, blue_row, alpha_row, constant_row)`

It can be easier to visualize colour matrices by spacing them outs:
```dm
var/list/c_matrix = list(
  rr,rg,rb,
  gr,gg,gb,
  br,bg,bb)
```

## Example
Here are simple colour matrices that can be used to set the colour of an atom.
```dm
var/list/red_color_matrix    = list( 255, 0, 0,
                                     255, 0, 0,
                                     255, 0, 0 )

var/list/green_color_matrix  = list( 0, 255, 0,
                                     0, 255, 0,
                                     0, 255, 0 )

var/list/blue_color_matrix   = list( 0, 0, 255,
                                     0, 0, 255,
                                     0, 0, 255 )
```
We can use the colours above to change the colour of any atom as follows:
```dm
mob/proc/SetColor(new_color)
  switch(new_color)
    if("red")
      color = red_color_matrix
    if("green")
      color = green_color_matrix
    if("blue")
      color = blue_color_matrix
```

Reading a color var that has been set to a matrix will return
the full 20-item list, where every 4 items represent a row in the matrix
(without the fifth column). 

> [!TIP] 
> **See also:**
> +   [color var (atom)](/ref/atom/var/color.md) 
> +   [color var (client)](/ref/client/var/color.md) 
> +   [MapColors proc (icon)](/ref/icon/proc/MapColors.md)
> +   [Rainmeter ColorMatrix Guide (external link)](https://docs.rainmeter.net/tips/colormatrix-guide)
