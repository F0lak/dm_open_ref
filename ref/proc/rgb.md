
## rgb (proc)

**Format:**
+   rgb(R,G,B)
+   rgb(R,G,B,A)
+   rgb(x,y,z,space=)
+   rgb(x,y,z,a,space)

**Arguments:**
+   R,G,B: Numbers from 0-255 corresponding to the red, green, and blue
components of a color.
+   A: Optional alpha component; 0 is transparent, 255 is opaque.
+   x,y,z: Color components for a different color space
+   space: ; defaults to [Color space](/ref/{{appendix}}/color-space)

**Returns:**
+   A color, represented by a text string in #RRGGBB or #RRGGBBAA format
***
A way of representing a color to be used in conjunction with icon arithmetic, atom.color, or other effects. The colors `rgb(0,0,0)` and `rgb(255,255,255)` represent black and white, two corners of the "color cube".


```dm

mob/proc/hurtme() // make a mob look damaged by adding red to its icon
  src.icon += rgb(20,0,0)

```


This proc returns a text string in the form used by HTML (#RRGGBB). rgb(255,0,128) for example becomes "#ff0080". If you use an alpha component, the format is #RRGGBBAA. You can use strings like this in most procs that use colors such as icon blending operations, and you can also use the short form #RGB or #RGBA. So if you know in advance that you want to use the color white, you can simply use"#fff" instead of rgb(255,255,255).

You can create colors other ways by specifying a different <a href="#/{{appendix}}/color-space">color space</a>. A color space can be specified by using a <a href="#/proc/arguments/named">named</a> "space" argument, or by using a 5-argument format (you can leave the alpha value blank or null to skip it), or by using named arguments for the other components.


```dm

// All of these lines are equivalent.
// They create (0,100,50) in HSL which is red (#ff0000).
src << rgb(0, 100, 50, space=COLORSPACE_HSL)
src << rgb(0, 100, 50, , COLORSPACE_HSL)
src << rgb(h=0, s=100, l=50)

```


Named arguments that are valid in `rgb()` are:

With the exception of `space`, only the first letter of the argument name matters, so `r` and `red` are the same thing.
***
**Related Pages:**
+    [rgb2num proc](/ref/proc/rgb2num)
+    [gradient proc](/ref/proc/gradient)
+    [Color space](/ref/{{appendix}}/color-space)
+    [HTML colors](/ref/{{appendix}}/html-colors)
+    [color var (atom)](/ref/atom/var/color)
+    [Blend proc (icon)](/ref/icon/proc/Blend)
+    [Color matrix](/ref/{notes}/color-matrix)
+    [Color matrix filter](/ref/{notes}/filters/color)
+    [Particle effects](/ref/{notes}/particles)
