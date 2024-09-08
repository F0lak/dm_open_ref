[]{#/{skin}/param/inner-size}
## inner-size parameter (skin) {#inner-size-parameter-skin byondver="513"}
**See also:**
:   [size parameter](#/%7Bskin%7D/param/size)
:   [outer-size parameter](#/%7Bskin%7D/param/outer-size)
:   [inner-pos parameter](#/%7Bskin%7D/param/inner-pos)
<!-- -->
**Applies to:**
:   [Main](#/%7Bskin%7D/control/main)
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
[can-scroll](#/%7Bskin%7D/param/can-scroll){.code} is true, this is the
size of the display area not including the scrollbars.