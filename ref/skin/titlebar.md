## titlebar parameter (skin)
**See also:**
*   [can-close parameter](/ref/%7Bskin%7D/param/can-close.md) -m
*   [can-minimize parameter](/ref/%7Bskin%7D/param/can-minimize.md) -m
*   [can-resize parameter](/ref/%7Bskin%7D/param/can-resize.md) -m
*   [icon parameter](/ref/%7Bskin%7D/param/icon.md) -m
*   [title parameter](/ref/%7Bskin%7D/param/title.md) -m
*   [use-title parameter](/ref/%7Bskin%7D/param/use-title.md) -m
*   [statusbar parameter](/ref/%7Bskin%7D/param/statusbar.md) -m
*   [is-fullscreen parameter](/ref/%7Bskin%7D/param/is-fullscreen.md) -m
*   [name var (world)](/ref/world/var/name.md) -m
<!-- -->
**Applies to:**
*   [Main](/ref/%7Bskin%7D/control/main.md) -m(window only)
<!-- -->
**Format:**
*   true/false
<!-- -->
**Default value:**
*   true


Show a titlebar for this window. This is also required for the
close, minimize, and maximize buttons to appear. 

If
`is-fullscreen` is true, `titlebar` is ignored, so this value represents
the state of the window when `is-fullscreen` is turned off again.