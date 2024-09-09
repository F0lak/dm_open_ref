[]{#/{skin}/param/titlebar}    
## titlebar parameter (skin)    
**See also:**    
:   [can-close parameter](/ref/%7Bskin%7D/param/can-close/can-close.md)    
:   [can-minimize parameter](/ref/%7Bskin%7D/param/can-minimize/can-minimize.md)    
:   [can-resize parameter](/ref/%7Bskin%7D/param/can-resize/can-resize.md)    
:   [icon parameter](/ref/%7Bskin%7D/param/icon/icon.md)    
:   [title parameter](/ref/%7Bskin%7D/param/title/title.md)    
:   [use-title parameter](/ref/%7Bskin%7D/param/use-title/use-title.md)    
:   [statusbar parameter](/ref/%7Bskin%7D/param/statusbar/statusbar.md)    
:   [is-fullscreen parameter](/ref/%7Bskin%7D/param/is-fullscreen/is-fullscreen.md)    
:   [name var (world)](/ref/world/var/name/name.md)    
<!-- -->    
**Applies to:**    
:   [Main](/ref/%7Bskin%7D/control/main/main.md) (window only)    
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