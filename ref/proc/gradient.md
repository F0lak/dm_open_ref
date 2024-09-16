## gradient proc

<!-- -->
**Format:**
+   gradient(Item1, Item2, \..., index)
+   gradient(Gradient, index)
<!-- -->
**Args:**
+   Gradient: A [color gradient](/ref/notes/color-gradient.md)  list
+   Item1, Item2\...: Elements of a [color
    gradient](/ref/notes/color-gradient.md)  list
+   index: The index along the gradient where the interpolation is done.
<!-- -->
**Returns:**
+   A color, represented by a text string in #RRGGBB or #RRGGBBAA format


Interpolates between two or more colors along a [color
gradient](/ref/notes/color-gradient.md) . By default, gradients extend
from an index of 0 to 1, but they are allowed to go beyond that if you
choose. 

The simplest way to use this proc is to interpolate
between two colors:
### Example:

``` dm
 // 20% of the way from red to black // prints #cc0000
which is rgb(204,0,0) src \<\< gradient(\"red\", \"black\", 0.2)

```
 

Anything that applies to color gradients can be used
in this proc, so you can have a looping gradient, or a gradient that
uses a color space other than RGB. 

In the first format where
you specify all the items separately, you can use [named
arguments](/ref/proc/arguments/named.md) for `index` and `space` (the
gradient\'s color space). If you don\'t specify an argument called
\"index\", the last argument is assumed to be the index.
### Example:

``` dm
 // This gradient loops through all the hues and goes from
0 to 6. // Because this is a looping gradient, index=10 becomes index=4.
// In HSL, this will give you blue (#0000ff). src \<\< gradient(0,
\"#f00\", 3, \"#0ff\", 6, \"#f00\", \"loop\", space=COLORSPACE_HSL,
index=10) 
```
 

The `gradient(Gradient, index)` format is
used for cases where you want to pass an existing gradient to the proc.
### Example:

``` dm
 var/candy_cane_gradient =
list(0.5,\"red\",0.5,\"white\",\"loop\") // the color output alternates
between red and white depending on the current time src \<\<
gradient(candy_cane_gradient, world.time/100) 
```


> [!TIP] 
> **See also:**
> +   [Color gradient](/ref/notes/color-gradient.md) 
> +   [rgb proc](/ref/proc/rgb.md) 
> +   [rgb2num proc](/ref/proc/rgb2num.md) 
> +   [Color space](/ref/appendix/color-space.md) 