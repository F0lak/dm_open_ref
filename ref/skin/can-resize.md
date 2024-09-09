[]{#/{skin}/param/can-resize}    
## can-resize parameter (skin)    
**See also:**    
:   [on-size parameter](ref/%7Bskin%7D/param/on-size)    
:   [can-minimize parameter](ref/%7Bskin%7D/param/can-minimize)    
:   [titlebar parameter](ref/%7Bskin%7D/param/titlebar)    
:   [is-fullscreen parameter](ref/%7Bskin%7D/param/is-fullscreen)    
<!-- -->    
**Applies to:**    
:   [Main](ref/%7Bskin%7D/control/main) (window only)    
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