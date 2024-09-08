[]{#/client/proc/MouseDown}
## MouseDown proc (client)
**See also:**
:   [Click proc (client)](#/client/proc/Click)
:   [DblClick proc (client)](#/client/proc/DblClick)
:   [MouseDown proc (atom)](#/atom/proc/MouseDown)
:   [MouseDrag proc (client)](#/client/proc/MouseDrag)
:   [MouseDrop proc (client)](#/client/proc/MouseDrop)
:   [MouseEntered proc (client)](#/client/proc/MouseEntered)
:   [MouseExited proc (client)](#/client/proc/MouseExited)
:   [MouseMove proc (client)](#/client/proc/MouseMove)
:   [MouseUp proc (client)](#/client/proc/MouseUp)
:   [MouseWheel proc (client)](#/client/proc/MouseWheel)
:   [mouse_opacity var (atom)](#/atom/var/mouse_opacity)
:   [mouse_pointer_icon var (client)](#/client/var/mouse_pointer_icon)
:   [show_popup_menus var (client)](#/client/var/show_popup_menus)
<!-- -->
**Format:**
:   MouseDown(object,location,control,params)
<!-- -->
**Args:**
:   object: the object under the mouse pointer
:   location: the turf, stat panel, grid cell, etc. containing the
    object where it was clicked
:   control: the name of the skin control involved
:   params: other parameters including mouse/keyboard flags, icon
    offsets, etc.; see [mouse handling](#/DM/mouse)
<!-- -->
**Default action:**
:   Call object.MouseDown(location,control,params).
This is called when the a mouse button is pressed while pointing to the
object. Note that MouseUp() will always be called after MouseDown() is
called, even if over empty space. That means `object`{.variable} and
`location`{.variable} may be null.
Don\'t define this unless you need it, because it generates extra
communication that is otherwise avoided. Most operations can be done
through `Click()`, `DblClick()`, and `MouseDrop()`. The other procedures
are simply available for completeness.
The argument format for this verb is: MouseDown(object as null\|atom in
usr.client,\\ location as null\|turf\|text in usr.client,\\ control as
text, params as text)
Note: In BYOND 3.5 this procedure took three different arguments:
`location`, `icon_x`, and `icon_y`. Since `icon_x` and `icon_y` have
been replaced, old code will need to be modified. Games compiled before
this change will still work normally.