## Blend proc (icon)

**Format:**
+   Blend(icon, function=ICON_ADD, x=1, y=1)
<!-- -->
**Args:**
+   icon: an icon file, /icon object, or color
+   function: the blending operation to use
+   x, y: the position to blend the icon

The valid blending operations are:
-   ICON_ADD
-   ICON_SUBTRACT
-   ICON_MULTIPLY
-   ICON_OVERLAY
-   ICON_AND
-   ICON_OR
-   ICON_UNDERLAY

The result is a combination of each corresponding pixel in the
two icons. In all but ICON_OVERLAY, ICON_UNDERLAY, and ICON_OR, the
transparent regions of the two icons are ORed together. That means if
either icon is transparent on a given pixel, the result will be
transparent. With ICON_OVERLAY or ICON_UNDERLAY, on the other hand, the
original icon shows through wherever the top icon is transparent, giving
the same effect as an overlay object, but resulting in only a single
icon. In ICON_OR, the transparent regions are ANDed together; solid
pixels are added together where they exist in both icons, or just pass
through if the other icon is transparent at that pixel. 

In addition to blending with an icon, an rgb() value may also be specified.
This is treated identically to an icon of that same solid color, except
that the x and y arguments will be ignored. Blending with a color blends
the whole icon. 

By default, the icons will line up at their
lower left corners. If you want to position the second icon in a
different place for blending, use the x and y arguments to specify where
its lower left corner will be. 1,1 is the default, which is the lower
left. 11,1 for instance would be 10 pixels to the right, and 1,21 would
be 20 pixels up.

> [!TIP] 
> **See also:**
> +   [icon](/ref/icon.md) 
> +   [procs (icon)](/ref/icon/proc.md) 
> +   [overlays var (atom)](/ref/atom/var/overlays.md) 
> +   [rgb proc](/ref/proc/rgb.md)