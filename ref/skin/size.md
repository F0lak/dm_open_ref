[]{#/{skin}/param/size}    
## size parameter (skin)    
**See also:**    
:   [pos parameter](/ref/%7Bskin%7D/param/pos)    
:   [anchor1, anchor2 parameters](/ref/%7Bskin%7D/param/anchor)    
:   [on-size parameter](/ref/%7Bskin%7D/param/on-size)    
:   [inner-size parameter](/ref/%7Bskin%7D/param/inner-size)    
:   [outer-size parameter](/ref/%7Bskin%7D/param/outer-size)    
<!-- -->    
**Applies to:**    
:   [All](/ref/%7Bskin%7D/control)    
<!-- -->    
**Format:**    
:   *width*x*height*    
The size of this control.    
Setting 0 for width or height uses up any available space    
right/downward.    
If the control is a window, this refers to its *interior size when not    
maximized or minimized*. That is, it does not count borders, titlebar,    
menu, or statusbar, and if the window is minimized/maximized, this    
refers to the window\'s normal size when it is restored. See the    
[inner-size](/ref/%7Bskin%7D/param/inner-size){.code} and    
[outer-size](/ref/%7Bskin%7D/param/outer-size){.code} params for    
comparison.    
If this control is a pane and    
[can-scroll](/ref/%7Bskin%7D/param/can-scroll){.code} is true, `size`    
refers to the total scrollable size of the pane, NOT the smaller size    
displayed. In this case, `outer-size` and `inner-size` refer to the    
display area with and without scrollbars, respectively.  