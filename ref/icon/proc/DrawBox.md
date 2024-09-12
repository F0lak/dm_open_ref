## DrawBox proc (icon)
**See also:**
+   [icon](/ref/icon.md) 
+   [procs (icon)](/ref/icon/proc.md) 
+   [rgb proc](/ref/proc/rgb.md) <!-- -->
**Format:**
+   DrawBox(rgb,x1,y1,x2=x1,y2=y1)
<!-- -->
**Args:**
+   rgb: `rgb(red,green,blue)` or `null`
+   x1,y1: Coordinates of one corner of the rectangle (1,1 is the lower
    left)
+   x2,y2: (optional) Coordinates of the other corner


A rectangle (filled) of the given color is drawn over every
frame in the icon. If x2 and/or y2 are omitted, a line or a single pixel
is drawn. To draw a transparent box instead of an opaque color, use null
as the color.