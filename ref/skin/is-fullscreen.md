[]{#/is-fullscreen parameter (skin).md}/param/is-fullscreen}    
## is-fullscreen parameter (skin) {#is-fullscreen-parameter-skin byondver="515"}    
**See also:**    
:   [can-resize parameter]/%7Bskin%7D/param/can-resize    
:   [titlebar parameter]/%7Bskin%7D/param/titlebar    
:   [is-maximized parameter]/%7Bskin%7D/param/is-maximized    
:   [is-minimized parameter]/%7Bskin%7D/param/is-minimized    
:   [size parameter]/%7Bskin%7D/param/size    
:   [outer-size parameter]/%7Bskin%7D/param/outer-size    
:   [screen-pos parameter]/%7Bskin%7D/param/screen-pos    
:   [screen-size parameter]/%7Bskin%7D/param/screen-size    
<!-- -->    
**Applies to:**    
:   [Main]/%7Bskin%7D/control/main (window only)    
<!-- -->    
**Format:**    
:   true/false    
<!-- -->    
**Default value:**    
:   false    
True if the window should be in fullscreen mode. This suppresses    
`can-resize`, `titlebar`, `is-maximized`, and `is-minimized`. They will    
continue to return the values that would apply if fullscreen mode were    
turned off.  