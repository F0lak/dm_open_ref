## size parameter (skin)

<!-- -->
**Applies to:**
+   [All](/ref/skin/control.md) 
<!-- -->
**Format:**
+   *width*x*height*


The size of this control. 

Setting 0 for width or
height uses up any available space right/downward. 

If the
control is a window, this refers to its *interior size when not
maximized or minimized*. That is, it does not count borders, titlebar,
menu, or statusbar, and if the window is minimized/maximized, this
refers to the window\'s normal size when it is restored. See the
[inner-size](/ref/skin/param/inner-size.md)  and
[outer-size](/ref/skin/param/outer-size.md)  params for
comparison. 

If this control is a pane and
[can-scroll](/ref/skin/param/can-scroll.md) is true, `size`
refers to the total scrollable size of the pane, NOT the smaller size
displayed. In this case, `outer-size` and `inner-size` refer to the
display area with and without scrollbars, respectively.

> [!TIP] 
> **See also:**
> +   [pos parameter](/ref/skin/param/pos.md) 
> +   [anchor1, anchor2 parameters](/ref/skin/param/anchor.md) 
> +   [on-size parameter](/ref/skin/param/on-size.md) 
> +   [inner-size parameter](/ref/skin/param/inner-size.md) 
> +   [outer-size parameter](/ref/skin/param/outer-size.md) 