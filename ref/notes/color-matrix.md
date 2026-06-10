
## color-matrix (info)
***
A color matrix is used to transform colors, in the same way that a matrix represented by the `/matrix` datum is used to transform 2D coordinates. A transformation matrix is 3x3, of which only 6 values are needed because the last column is always the same. A color matrix, because it transforms four different numbers instead of two, is 5x5.

In that formula, values like `rg` mean "red to green", meaning that's the ratio of red in of green out. (The "c" is for "constant".) In an identity matrix, which just produces the original color, the values `rr`, `gg`, `bb`, and `aa` are all 1 and everything else is 0.

In easier-to-understand terms, this is how the result is calculated:


```dm

new_red   = red * rr + green * gr + blue * br + alpha * ar + 255 * cr
new_green = red * rg + green * gg + blue * bg + alpha * ag + 255 * cg
new_blue  = red * rb + green * gb + blue * bb + alpha * ab + 255 * cb
new_alpha = red * ra + green * ga + blue * ba + alpha * aa + 255 * ca

```


It is helpful to think of each row in the matrix as what each component of the original color will become. The first row of the matrix is the rgba value you'll get for each unit of red; the second is what each green becomes, and so on.

Because the fifth column of the matrix is always the same, only 20 of the values need to be provided. You can use a color matrix with atom.color or client.color in any of the following ways:

Reading a color var that has been set to a matrix will return the full 20-item list, where every 4 items represent a row in the matrix (without the fifth column).

In the `MapColors()` icon proc, the values are sent as arguments, not as a list.

The <a href="#/{notes}/filters/color">color filter</a> allows the use of other color spaces for a matrix. In those other color spaces, the matrix calculations work the same but instead of red, green, and blue, they'll be whatever values that color space uses. For instance an HSL color matrix uses hue in place of red, saturation in place of green, and luminance in place of blue. (Alpha is always alpha.)

The way that works internally is that the shader will convert a color from RGB to the color space used by the matrix, then apply the matrix, then convert back to RGB.
***