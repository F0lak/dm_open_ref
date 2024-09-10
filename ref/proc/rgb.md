[]{#/rgb proc.md}    
## rgb proc    
**See also:**    
:   [rgb2num proc](/rgb proc.md2num)    
:   [gradient proc](/proc/gradient)    
:   [Color space](/%7B%7Bappendix%7D%7D/color-space)    
:   [HTML colors](/%7B%7Bappendix%7D%7D/html-colors)    
:   [color var (atom)](/atom/var/color)    
:   [Blend proc (icon)](/icon/proc/Blend)    
:   [Color matrix](/%7Bnotes%7D/color-matrix)    
:   [Color matrix filter](/%7Bnotes%7D/filters/color)    
:   [Particle effects](/%7Bnotes%7D/particles)    
<!-- -->    
**Format:**    
:   rgb(R,G,B)    
:   rgb(R,G,B,A)    
:   rgb(x,y,z,space=*color space*)    
:   rgb(x,y,z,a,space)    
<!-- -->    
**Args:**    
:   R,G,B: Numbers from 0-255 corresponding to the red, green, and blue    
    components of a color.    
:   A: Optional alpha component; 0 is transparent, 255 is opaque.    
:   x,y,z: Color components for a different color space    
:   space: [Color space](/%7B%7Bappendix%7D%7D/color-space); defaults    
    to `COLORSPACE_RGB`    
<!-- -->    
**Returns:**    
:   A color, represented by a text string in #RRGGBB or #RRGGBBAA format    
A way of representing a color to be used in conjunction with icon    
arithmetic, atom.color, or other effects. The colors `rgb(0,0,0)` and    
`rgb(255,255,255)` represent black and white, two corners of the \"color    
cube\".    
### Example:    
mob/proc/hurtme() // make a mob look damaged by adding red to its icon    
src.icon += rgb(20,0,0)    
This proc returns a text string in the form used by HTML (#RRGGBB).    
rgb(255,0,128) for example becomes \"#ff0080\". If you use an alpha    
component, the format is #RRGGBBAA. You can use strings like this in    
most procs that use colors such as icon blending operations, and you can    
also use the short form #RGB or #RGBA. So if you know in advance that    
you want to use the color white, you can simply use\"#fff\" instead of    
rgb(255,255,255).    
You can create colors other ways by specifying a different [color    
space](/%7B%7Bappendix%7D%7D/color-space). A color space can be    
specified by using a [named](/proc/arguments/named) \"space\" argument,    
or by using a 5-argument format (you can leave the alpha value blank or    
null to skip it), or by using named arguments for the other components.    
### Example:    
// All of these lines are equivalent. // They create (0,100,50) in HSL    
which is red (#ff0000). src \<\< rgb(0, 100, 50, space=COLORSPACE_HSL)    
src \<\< rgb(0, 100, 50, , COLORSPACE_HSL) src \<\< rgb(h=0, s=100,    
l=50)    
Named arguments that are valid in `rgb()` are:    
-   `space`    
-   `red`    
-   `green`    
-   `blue`    
-   `alpha`    
-   `hue`    
-   `saturation`    
-   `chroma`    
-   `value`    
-   `luminance`    
-   `y` (HCY luminance)    
With the exception of `space`, only the first letter of the argument    
name matters, so `r` and `red` are the same thing.  