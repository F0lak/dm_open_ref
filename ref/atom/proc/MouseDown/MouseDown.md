[]{#/atom/proc/MouseDown}
## MouseDown proc (atom)
**See also:**
:   [Click proc (atom)](#/atom/proc/Click)
:   [DblClick proc (atom)](#/atom/proc/DblClick)
:   [MouseDown proc (client)](#/client/proc/MouseDown)
:   [MouseDrag proc (atom)](#/atom/proc/MouseDrag)
:   [MouseDrop proc (atom)](#/atom/proc/MouseDrop)
:   [MouseEntered proc (atom)](#/atom/proc/MouseEntered)
:   [MouseExited proc (atom)](#/atom/proc/MouseExited)
:   [MouseMove proc (atom)](#/atom/proc/MouseMove)
:   [MouseUp proc (atom)](#/atom/proc/MouseUp)
:   [MouseWheel proc (atom)](#/atom/proc/MouseWheel)
:   [mouse_drag_pointer var (atom)](#/atom/var/mouse_drag_pointer)
:   [mouse_drop_pointer var (atom)](#/atom/var/mouse_drop_pointer)
:   [mouse_opacity var (atom)](#/atom/var/mouse_opacity)
:   [mouse_over_pointer var (atom)](#/atom/var/mouse_over_pointer)
:   [show_popup_menus var (client)](#/client/var/show_popup_menus)
<!-- -->
**Format:**
:   MouseDown(location,control,params)
<!-- -->
**Args:**
:   location: the turf, stat panel, grid cell, etc. in which the object
    was clicked
:   control: the name of the skin control involved
:   params: other parameters including mouse/keyboard flags, icon
    offsets, etc.; see [mouse handling](#/DM/mouse)
This is called when a mouse button is pressed while pointing to this
object.
Don\'t define this unless you need it, because it generates extra
communication that is otherwise avoided. Most operations can be done
through `Click()`, `DblClick()`, and `MouseDrop()`. The other procedures
are simply available for completeness.
Note: In BYOND 3.5 this procedure took three different arguments:
`location`, `icon_x`, and `icon_y`. Since `icon_x` and `icon_y` have
been replaced, old code will need to be modified. Games compiled before
this change will still work normally.