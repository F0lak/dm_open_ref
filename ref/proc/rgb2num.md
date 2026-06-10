
## rgb2num (proc)

**Format:**
+   rgb2num(color)
+   rgb2num(color, space)

**Arguments:**
+   color: A color value (see ) [HTML colors](/ref/{{appendix}}/html-colors)
+   space: ; default is [Color space](/ref/{{appendix}}/color-space)

**Returns:**
+   A list with the components of this color
***
Parses a color into a list with 3 or 4 component values; the 4th value is alpha, if it's part of the color provided.


```dm

var/list/RGB = rgb2num("#ff8000")
src << RGB[1]     // red (255)
src << RGB[2]     // green (128)
src << RGB[3]     // blue (0)

```


By specifying a different color space, you can convert a color into a different format.


```dm

var/list/HSL = rgb2num("#5af", COLORSPACE_HSL)
src << HSL[1]     // hue (210)
src << HSL[2]     // saturation (100)
src << HSL[3]     // luminance (66.6667)

```

***
**Related Pages:**
+    [rgb proc](/ref/proc/rgb)
+    [gradient proc](/ref/proc/gradient)
+    [Color space](/ref/{{appendix}}/color-space)
+    [HTML colors](/ref/{{appendix}}/html-colors)
