## Displacement map filter 
###### BYOND Version 513

Format:
+   filter(type="displace", ...)

Args:
+   x: Horizontal offset of map (defaults to 0)
+   y: Vertical offset of map (defaults to 0)
+   size: Maximum distortion, in pixels
+   icon: Icon to use as a displacement map
+   render_source: `render_target` to use as a displacement map
+   flags: Defaults to 0; use see below for other flags

> [!TIP]
> Amylizzle made a tool to create and test displacement maps.
> You can check it out and download it [Here](https://github.com/amylizzle/displacemaptester)

Uses an icon or render target as a template for various warping
effects on the main image. Think of displacement as "pulling" a pixel from an offset
location.

In the displacement map, pixels that
have a higher red component will make the image appear to warp to the
left, lower reds warp it to the right, and gray (r=128) will cause no
horizontal warping. The green component affects the vertical: higher to
warp upward, lower to warp downward. Transparent pixels in the
displacement map will have no effect. 

This can be used for very complex distortion,
unlike other distortion filters such as wave and
ripple that are confined to specific equations.

The optional `FILTER_OVERLAY` flag is supported for the
`flags` argument, which will overlay the displaced image onto the
original.

> [!TIP] 
> **See also:**
> +   [Alpha mask (filters)](/ref/notes/filters/alpha.md) 
> +   [icon var (atom)](/ref/atom/var/icon.md) 
> +   [render_target var (atom)](/ref/atom/var/render_target.md)
