[]{#/{skin}/param/can-resize}    
## can-resize parameter (skin)    
**See also:**    
:   [on-size parameter](/ref/%7Bskin%7D/param/on-size/on-size.md)    
:   [can-minimize parameter](/ref/%7Bskin%7D/param/can-minimize/can-minimize.md)    
:   [titlebar parameter](/ref/%7Bskin%7D/param/titlebar/titlebar.md)    
:   [is-fullscreen parameter](/ref/%7Bskin%7D/param/is-fullscreen/is-fullscreen.md)    
<!-- -->    
**Applies to:**    
:   [Main](/ref/%7Bskin%7D/control/main/main.md) (window only)    
<!-- -->    
**Format:**    
:   true/false    
<!-- -->    
**Default value:**    
:   true    
Allow the window to be resized or maximized.    
If `is-fullscreen` is true, `can-resize` is ignored, so this value    
represents the state of the window when `is-fullscreen` is turned off    
again.  