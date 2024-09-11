## view-size parameter (skin)
**See also:**
*   [letterbox parameter](/ref/%7Bskin%7D/param/letterbox.md) -m
*   [zoom parameter](/ref/%7Bskin%7D/param/zoom.md) -m
*   [zoom-mode parameter](/ref/%7Bskin%7D/param/zoom-mode.md) -m
*   [icon_size var (world)](/ref/world/var/icon_size.md) -m
*   [view var (world)](/ref/world/var/view.md) -m
*   [view var (client)](/ref/client/var/view.md) -m
*   [HUD / screen objects](/ref/%7Bnotes%7D/HUD.md) -m
<!-- -->
**Applies to:**
*   [Map](/ref/%7Bskin%7D/control/map.md) -m (window only)
<!-- -->
**Format:**
*   *width*x*height*


The size, in pixels, of the map after `zoom` has been applied.


For instance, if the client view has 10×10 tiles (this includes
any extended tiles caused by HUD objects) and `world.icon_size` is
32x32, the map has a native size of 320×320 pixels. If the map has a
zoom level of 2, then `view-size` will be 640x640. 

With a
`zoom` value of 0, which is the default for most projects, the actual
zoom level is automatically determined by the size of the map control,
the map\'s native pixel size as explained above, and the value of the
[letterbox](/ref/%7Bskin%7D/param/letterbox.md) -m.code} parameter.