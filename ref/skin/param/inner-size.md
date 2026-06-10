
## inner-size (info)
***
Read-only.

If the control is a window, this refers to its current interior size: i.e., not counting titlebar, statusbar, borders, etc. If it's maximized, this will be the true size of the window interior, as opposed to `size` which is the interior size once this window is no longer maximized.

If this control is a pane and <a class="code" href="#/{skin}/param/can-scroll">can-scroll</a> is true, this is the size of the display area not including the scrollbars.
***