## outer-size parameter (skin) 
###### BYOND Version 513

<!-- -->
**Applies to:**
+   [Main](/ref/%7Bskin%7D/control/main.md) 
<!-- -->
**Format:**
+   *width*x*height*


Read-only. 

If the control is a window, this refers to
its current exterior size *including* titlebar, statusbar, borders, etc.
If the window is maximized, this is the maximized size. 

If this
control is a pane and [can-scroll](/ref/%7Bskin%7D/param/can-scroll.md)
is true, this is the size of the display area including the scrollbars.

**See also:**
+   [size parameter](/ref/%7Bskin%7D/param/size.md) 
+   [inner-size parameter](/ref/%7Bskin%7D/param/inner-size.md) 