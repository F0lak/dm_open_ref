## Color matrix filter 
###### BYOND Version 513
**See also:**
*   [color var (atom)](/atom/var/color)
*   [Color matrix](/%7Bnotes%7D/color-matrix)
*   [Color space](/%7B%7Bappendix%7D%7D/color-space)
<!-- -->
Format:
*   filter(type=\"color\", \...)
<!-- -->
Args:
*   color* A color matrix
*   space* Value indicating color space* defaults to `FILTER_COLOR_RGB`


Applies a color matrix to this image. Unlike with the
atom.color var, you can apply color conversions other than the regular
RGBA color space, depending on the value of `space`. See [Color
space](/%7B%7Bappendix%7D%7D/color-space) for more information.