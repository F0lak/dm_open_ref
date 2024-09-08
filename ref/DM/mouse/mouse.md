[]{#/DM/mouse toc="mouse handling"}
## mouse handling
Various mouse actions may be handled by defining procedures either on
the client object or on the atomic object being manipulated. Any of the
following procedures may be defined:
-   [MouseDown()](#/client/proc/MouseDown)
-   [MouseUp()](#/client/proc/MouseUp)
-   [MouseDrag()](#/client/proc/MouseDrag)
-   [MouseDrop()](#/client/proc/MouseDrop)
-   [MouseEntered()](#/client/proc/MouseEntered)
-   [MouseExited()](#/client/proc/MouseExited)
-   [MouseMove](#/client/proc/MouseMove)
-   [MouseWheel](#/client/proc/MouseWheel)
-   [Click()](#/client/proc/Click)
-   [DblClick()](#/client/proc/DblClick)
In general, define only the procedures you need, because extra
communication overhead may be avoided when the compiler detects that you
do not care about certain events.
The arguments used in mouse procs generally follow one of these forms:
For Click(), DblClick(), MouseDown(), MouseUp(), MouseEntered(), MouseExited(), and MouseMove():
:   client/Click(object, location, control, params)\
    atom/Click(location, control, params)
For MouseDrag() and MouseDrop():
:   client/MouseDrag(src_object, over_object, src_location,
    over_location, src_control, over_control, params)\
    atom/MouseDrag(over_object, src_location, over_location,
    src_control, over_control, params)
For MouseWheel():
:   client/MouseWheel(object, delta_x, delta_y, location, control,
    params)\
    atom/MouseWheel(delta_x, delta_y, location, control, params)
The `location` argument varies with the type of control. For the map, it
will be the turf where the mouse action happened. For info controls
(statpanels), it will be the name of the statpanel where the action
happened. For grid controls, it will be the cell where the action
happened. For others controls it may vary, but most will leave this
blank.
The `control` argument is the ID of the skin control where the action
happened, such as `"mappane.map"` or `"mainwindow.banner"`.
The `params` argument is text, and can be converted to a list using
[params2list()](#/proc/params2list){.code}. It may contain any of the
following properties, which will only be set if they are used:
-   icon-x, icon-y: Pixel coordinates within the icon, in the icon\'s
    coordinate space
-   screen-loc: Pixel coordinates in screen_loc format
    (\"\[tile_x\]:\[pixel_x\],\[tile_y\]:\[pixel_y\]\")
-   left, middle, right: Mouse buttons pressed, held, or released in
    this action (see compatibility note below)
-   button: Mouse button pressed or released in this action (see
    compatibility note below)
-   ctrl, shift, alt: Keys held down during the mouse action
-   drag-cell, drop-cell: Cells involved if using a Grid control
-   drag: The button used for dragging (only sent for unrelated mouse
    up/down messages during a drag)
-   link: If the mouse is over a link in maptext, or this event is
    related to clicking such a link
-   vis-x, vis-y: Pixel coordinates relative to the icon\'s position on
    screen
The icon-x/y coordinates are integers, and try to point to the actual
pixel in the icon before any atom transforms are done; i.e. if the icon
were scaled up to 3 times its size using the transform var, then a 3×3
region of pixels would all have the same icon-x/y values. The lower left
pixel of the icon is 1,1. The vis-x/y parameters are screen-based, and
their origin (1,1) is wherever the lower left corner of the icon is
rendered.
Note: vis-x/y will not be included in the parameters if they are the
same as icon-x/y.
If the mouse is over an overlay, icon-x/y and vis-x/y are relative to
the parent object, not the overlay icon itself, so it\'s possible to
have value outside of the normal range of 1,1 to \[width\],\[height\].
The mouse pointer may be customized as well. The following variables all
deal with the appearance of the pointer. They do not control what
actions may be taken by the user, but they provide hints to the user
about what actions may work.
-   [mouse_pointer_icon](#/client/var/mouse_pointer_icon)
-   [mouse_over_pointer](#/atom/var/mouse_over_pointer)
-   [mouse_drag_pointer](#/atom/var/mouse_drag_pointer)
-   [mouse_drop_pointer](#/atom/var/mouse_drop_pointer)
-   [mouse_drop_zone](#/atom/var/mouse_drop_zone)
-   [mouse_opacity](#/atom/var/mouse_opacity)
When selecting a mouse pointer, you may provide your own custom icon or
use one of the [built-in pointers](#/DM/mouse/pointers).
Note: Older games compiled prior to BYOND 4.0 had a different format for
the `MouseDown()` and `MouseUp()` procs. These used `icon_x` and
`icon_y` as arguments, but `control` and `params` have replaced them.
Note: Games compiled before version 514 did not have the `button`
parameter, so they handled the `left`, `middle`, and `right` parameters
differently. In old versions, only the button used in the action (left,
middle, right) was included as a parameter; now all buttons being held
or changed are included, and `button` is the mouse button that changed.