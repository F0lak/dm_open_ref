[]{#/proc/rgb2num}    
## rgb2num proc    
**See also:**    
:   [rgb proc](/ref/proc/rgb.md)    
:   [gradient proc](/ref/proc/gradient.md)    
:   [Color space](/ref/%7B%7Bappendix%7D%7D/color-space.md)    
:   [HTML colors](/ref/%7B%7Bappendix%7D%7D/html-colors.md)    
<!-- -->    
**Format:**    
:   rgb2num(color)    
:   rgb2num(color, space)    
<!-- -->    
**Args:**    
:   color: A color value (see [HTML    
    colors](/ref/%7B%7Bappendix%7D%7D/html-colors.md))    
:   space: [Color space](/ref/%7B%7Bappendix%7D%7D/color-space.md); default is    
    `COLORSPACE_RGB`    
<!-- -->    
**Returns:**    
:   A list with the components of this color    
Parses a color into a list with 3 or 4 component values; the 4th value    
is alpha, if it\'s part of the color provided.    
### Example:    
var/list/RGB = rgb2num(\"#ff8000\") src \<\< RGB\[1\] // red (255) src    
\<\< RGB\[2\] // green (128) src \<\< RGB\[3\] // blue (0)    
By specifying a different color space, you can convert a color into a    
different format.    
### Example:    
var/list/HSL = rgb2num(\"#5af\", COLORSPACE_HSL) src \<\< HSL\[1\] //    
hue (210) src \<\< HSL\[2\] // saturation (100) src \<\< HSL\[3\] //    
luminance (66.6667)  