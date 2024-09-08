[]{#/{skin}/param/titlebar}
## titlebar parameter (skin)
**See also:**
:   [can-close parameter](#/%7Bskin%7D/param/can-close)
:   [can-minimize parameter](#/%7Bskin%7D/param/can-minimize)
:   [can-resize parameter](#/%7Bskin%7D/param/can-resize)
:   [icon parameter](#/%7Bskin%7D/param/icon)
:   [title parameter](#/%7Bskin%7D/param/title)
:   [use-title parameter](#/%7Bskin%7D/param/use-title)
:   [statusbar parameter](#/%7Bskin%7D/param/statusbar)
:   [is-fullscreen parameter](#/%7Bskin%7D/param/is-fullscreen)
:   [name var (world)](#/world/var/name)
<!-- -->
**Applies to:**
:   [Main](#/%7Bskin%7D/control/main) (window only)
<!-- -->
**Format:**
:   true/false
<!-- -->
**Default value:**
:   true
Show a titlebar for this window. This is also required for the close,
minimize, and maximize buttons to appear.
If `is-fullscreen` is true, `titlebar` is ignored, so this value
represents the state of the window when `is-fullscreen` is turned off
again.