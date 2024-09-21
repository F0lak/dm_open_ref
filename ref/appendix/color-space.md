# Color space

There are different ways of interpreting color besides RGB.
Several parts of BYOND are capable of using other color spaces.
### COLORSPACE_RGB

The default color space is RGB, where each color is split into
red, green, and blue components, as well as an optional alpha. All of
these components range from 0 to 255. 

The color yellow for
instance is `rgb(255,255,0)` which is red and green mixed together at
their maximum brightness, but no blue component.
### COLORSPACE_HSV

HSV stands for hue, saturation, and value.
-   Hue ranges from 0 to 360 on a color wheel, where 0 is red, 60 is
    yellow, 120 is green, and so on as seen in the image.
-   Saturation is how colorful this color is; it ranges from 0 which
    means a shade of gray, to 100 which is fully colored.
-   Value is the brightness of the biggest red, green, or blue
    component, and ranges from 0 to 100. A value of 0 is always black.

All pure hues such as red (hue=0) have a saturation of 100 and
a value of 100. As saturation decreases, the colors turns whiter. Lower
values mean darker colors and darker shades of gray. 

In HSV,
saturation is less meaningful as value gets closer to 0. Black of course
always has a value of 0. With 10 as the value, saturation=100 gives you
a very dark color whereas saturation=0 is a 10% shade of gray.
### COLORSPACE_HSL

HSL is a little more intuitive than HSV. Here, the value is
replaced by luminance, which again ranges from 0 to 100. Luminance is
the average of the minimum and maximum values of the red, green, and
blue components. 

Black has a luminance of 0; white has a
luminance of 100. Pure hues all have a saturation of 100 and luminance
of 50. As saturation decreases, the color will approach a grayscale
shade of L%. 

Saturation is less meaningful the closer luminance
is to 0 or 100. At a luminance of 100, the saturation is totally
irrelevant. At 90, high saturation will get you a very light shade of
the hue but that isn\'t very far off from a 90% shade of gray.
### COLORSPACE_HCY

HCY stands for **hue**, **chroma**, and the Y is for grayscale
luminance. (Again chroma and Y range from 0 to 100.) This color space is
based around the apparent brightness of each color according to a rough
approximation of human vision. 

Chroma is similar to saturation
in that it determines how far from grayscale the color is. As chroma
decreases toward 0, the color approaches a grayscale shade of Y%.
What\'s different about HCY color from HSV or HSL is that at chroma=0
and chroma=100 the colors should appear equally bright. Pure red,
therefore, has a hue of 0, a chroma of 100, and a Y luminance of only
29.9---roughly what red would look like in black & white with all the
color leached out.

> [!TIP] 
> **See also:**
> +   [rgb proc](/ref/proc/rgb.md) 
> +   [rgb2num proc](/ref/proc/rgb2num.md) 
> +   [gradient proc](/ref/proc/gradient.md) 
> +   [animate proc](/ref/proc/animate.md) 
> +   [Color gradient](/ref/notes/color-gradient.md) 
> +   [Color matrix filter](/ref/notes/filters/color.md) 