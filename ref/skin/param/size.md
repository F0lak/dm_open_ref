
## size (info)
***
The size of this control.

Setting 0 for width or height uses up any available space right/downward.

If the control is a window, this refers to its *interior size when not maximized or minimized*. That is, it does not count borders, titlebar, menu, or statusbar, and if the window is minimized/maximized, this refers to the window's normal size when it is restored. See the <a class="code" href="#/{skin}/param/inner-size">inner-size</a> and <a class="code" href="#/{skin}/param/outer-size">outer-size</a> params for comparison.

If this control is a pane and <a class="code" href="#/{skin}/param/can-scroll">can-scroll</a> is true, `size` refers to the total scrollable size of the pane, NOT the smaller size displayed. In this case, `outer-size` and `inner-size` refer to the display area with and without scrollbars, respectively.
***