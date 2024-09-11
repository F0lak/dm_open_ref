## Color gradient 
###### BYOND Version 514
**See also:**
*   [gradient proc](/proc/gradient)
*   [color var (atom)](/atom/var/color)
*   [Particle effects](/%7Bnotes%7D/particles)
*   [Color space](/%7B%7Bappendix%7D%7D/color-space)


A color gradient is a special list that defines a range of
colors that you can smoothly interpolate between. A simple example is a
gradient from red to white:
### Example:

```
 list(\"red\", \"white\") // OR list(0, \"red\", 1, \"white\")

```
 

Applying a number like 0.2 to this gradient would
give you a color that\'s 20% of the way from red to white. More complex
gradients however are also possible. 

The format of a gradient
is a list that contains a number (the position along the gradient, from
0 to 1 unless you use values outside that range) followed by a color.
You can have as complex a gradient as you like. If you reuse the same
number twice in a row, the gradient will have a sudden color change at
that point. 

It is also possible to skip numbers or colors, and
they will be filled in automatically with the previous number or color.
The exceptions are at the beginning and ends of the list; at the end of
the gradient, the last color is assigned a number 1 by default, and the
first is assigned 0. If you skip colors at the beginning, they will be
filled in with the first color you use. 

Include \"loop\"
anywhere in the list to make this a looped gradient. If you don\'t, any
numbers outside the gradient\'s range will be clamped to that range.
E.g., in a normal gradient ranging from 0 to 1, a number of 1.2 is
interpreted as 1 without a loop and 0.2 with a loop. 

Here are
some more examples:
### Example:

```
 // color wheel; ranges 0 to 6 and loops list(0, \"#f00\", 1,
\"#ff0\", 2, \"#0f0\", 3, \"#0ff\", 4, \"#00f\", 5, \"#f0f\", 6,
\"#f00\", \"loop\") // 10% each red, yellow, green, blue, with a 20%
transition zone between each // notice no color follows 0.4 or 0.7, so
the previous color is used list(0.1, \"#f00\", 0.3, \"#ff0\", 0.4, 0.6,
\"#008000\", 0.7, 0.9, \"#00f\") // green and black stripes list(0.5,
\"#008000\", 0.5, \"#000000\", \"loop\") 
```
 

You can
also include \"space\" in the list, and give it an associated value that
describes the color space this gradient uses to interpolate between
colors. For instance, `"space"=COLORSPACE_HSL` will use HSL
interpolation instead of the default RGB. See [Color
space](/%7B%7Bappendix%7D%7D/color-space) for more information.
### Example:

```
 // color wheel with a different color space list(0, \"#f00\",
3, \"#0ff\", 6, \"#f00\", \"loop\", \"space\"=COLORSPACE_HSLA)

```
 

Currently, color gradients are only used by particle
effects and the [`gradient` proc](/proc/gradient). With particles, if
you use a gradient the particle\'s color is given as a number, and that
number is used to look up its real color from the gradient. The number
can change over time, thus changing the particle\'s color.