## Scale proc (icon)

**Format:**
+   Scale(width, height)
<!-- -->
**Args:**
+   width,height: size of the new icon


The current icon is scaled to a new size. 

If
world.map_format is set to TILED_ICON_MAP and the new size is not in
multiples of world.icon_size, the icon will be padded with transparent
pixels to the top and right as needed. See map_format for more
information. 

Scale() automatically performs antialiasing to
avoid unwanted artifacts.

> [!TIP] 
> **See also:**
> +   [icon](/ref/icon.md) 
> +   [procs (icon)](/ref/icon/proc.md) 
> +   [icon_size var (world)](/ref/world/var/icon_size.md) 
> +   [map_format var (world)](/ref/world/var/map_format.md) 
> +   [Big icons](/ref/notes/big-icons.md) 
> +   [Tiled icons](/ref/notes/tiled-icons.md) <!-- -->