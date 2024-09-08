[]{#/atom/proc/MouseDrop}
## MouseDrop proc (atom)
**See also:**
:   [Click proc (atom)](#/atom/proc/Click)
:   [DblClick proc (atom)](#/atom/proc/DblClick)
:   [MouseDown proc (atom)](#/atom/proc/MouseDown)
:   [MouseDrag proc (atom)](#/atom/proc/MouseDrag)
:   [MouseDrop proc (client)](#/client/proc/MouseDrop)
:   [MouseEntered proc (atom)](#/atom/proc/MouseEntered)
:   [MouseExited proc (atom)](#/atom/proc/MouseExited)
:   [MouseMove proc (atom)](#/atom/proc/MouseMove)
:   [MouseUp proc (atom)](#/atom/proc/MouseUp)
:   [MouseWheel proc (atom)](#/atom/proc/MouseWheel)
:   [mouse_drag_pointer var (atom)](#/atom/var/mouse_drag_pointer)
:   [mouse_drop_pointer var (atom)](#/atom/var/mouse_drop_pointer)
:   [mouse_drop_zone var (atom)](#/atom/var/mouse_drop_zone)
:   [mouse_opacity var (atom)](#/atom/var/mouse_opacity)
:   [mouse_over_pointer var (atom)](#/atom/var/mouse_over_pointer)
:   [show_popup_menus var (client)](#/client/var/show_popup_menus)
<!-- -->
**Format:**
:   MouseDrop(over_object,src_location,over_location,src_control,over_control,params)
<!-- -->
**Args:**
:   over_object: the object under the mouse pointer
:   src_location: the turf, stat panel, grid cell, etc. from where the
    src object was dragged
:   over_location: the turf, stat panel, grid cell, etc. containing the
    object under the mouse pointer
:   src_control: The id of the skin control the object was dragged from
:   over_control: The id of the skin control the object was dropped onto
:   params: other parameters including mouse/keyboard flags, icon
    offsets, etc.; see [mouse handling](#/DM/mouse)
This is called when the a mouse button is released after dragging this
object. The over_object may be null if dropping over a stat panel or
over other empty space.