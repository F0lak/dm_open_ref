[]{#/{notes}/filters/color toc="Color matrix (filters)"}    
## Color matrix filter {#color-matrix-filter byondver="513"}    
**See also:**    
:   [color var (atom)](/ref/atom/var/color.md)    
:   [Color matrix](/ref/%7Bnotes%7D/color-matrix.md)    
:   [Color space](/ref/%7B%7Bappendix%7D%7D/color-space.md)    
<!-- -->    
Format:    
:   filter(type=\"color\", \...)    
<!-- -->    
Args:    
:   color: A color matrix    
:   space: Value indicating color space: defaults to `FILTER_COLOR_RGB`    
Applies a color matrix to this image. Unlike with the atom.color var,    
you can apply color conversions other than the regular RGBA color space,    
depending on the value of `space`. See [Color    
space](/ref/%7B%7Bappendix%7D%7D/color-space.md) for more information.  