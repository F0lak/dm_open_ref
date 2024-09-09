[]{#/{skin}/param/inner-size}    
## inner-size parameter (skin) {#inner-size-parameter-skin byondver="513"}    
**See also:**    
:   [size parameter](/ref/%7Bskin%7D/param/size/size.md)    
:   [outer-size parameter](/ref/%7Bskin%7D/param/outer-size/outer-size.md)    
:   [inner-pos parameter](/ref/%7Bskin%7D/param/inner-pos/inner-pos.md)    
<!-- -->    
**Applies to:**    
:   [Main](/ref/%7Bskin%7D/control/main/main.md)    
<!-- -->    
**Format:**    
:   *width*x*height*    
Read-only.    
If the control is a window, this refers to its current interior size:    
i.e., not counting titlebar, statusbar, borders, etc. If it\'s    
maximized, this will be the true size of the window interior, as opposed    
to `size` which is the interior size once this window is no longer    
maximized.    
If this control is a pane and    
[can-scroll](/ref/%7Bskin%7D/param/can-scroll/can-scroll.md){.code} is true, this is the    
size of the display area not including the scrollbars.  