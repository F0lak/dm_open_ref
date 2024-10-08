## view-size parameter (skin)


**Applies to:**
+   [Map](/ref/skin/control/map.md)  (window only)

**Format:**
+   *width*x*height*


The size, in pixels, of the map after `zoom` has been applied.


For instance, if the client view has 10×10 tiles (this includes
any extended tiles caused by HUD objects) and `world.icon_size` is
32x32, the map has a native size of 320×320 pixels. If the map has a
zoom level of 2, then `view-size` will be 640x640. 

With a
`zoom` value of 0, which is the default for most projects, the actual
zoom level is automatically determined by the size of the map control,
the map\'s native pixel size as explained above, and the value of the
[letterbox](/ref/skin/param/letterbox.md) parameter.

> [!TIP] 
> **See also:**
> +   [letterbox parameter](/ref/skin/param/letterbox.md) 
> +   [zoom parameter](/ref/skin/param/zoom.md) 
> +   [zoom-mode parameter](/ref/skin/param/zoom-mode.md) 
> +   [icon_size var (world)](/ref/world/var/icon_size.md) 
> +   [view var (world)](/ref/world/var/view.md) 
> +   [view var (client)](/ref/client/var/view.md) 
> +   [HUD / screen objects](/ref/notes/HUD.md) 