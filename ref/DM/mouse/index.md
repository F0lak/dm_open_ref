
## mouse (info)
***
Various mouse actions may be handled by defining procedures either on the client object or on the atomic object being manipulated. Any of the following procedures may be defined:

In general, define only the procedures you need, because extra communication overhead may be avoided when the compiler detects that you do not care about certain events.

The arguments used in mouse procs generally follow one of these forms:

The `location` argument varies with the type of control. For the map, it will be the turf where the mouse action happened. For info controls (statpanels), it will be the name of the statpanel where the action happened. For grid controls, it will be the cell where the action happened. For others controls it may vary, but most will leave this blank.

The `control` argument is the ID of the skin control where the action happened, such as `"mappane.map"` or `"mainwindow.banner"`.

The `params` argument is text, and can be converted to a list using <a class="code" href="#/proc/params2list">params2list()</a>. It may contain any of the following properties, which will only be set if they are used:

The icon-x/y coordinates are integers, and try to point to the actual pixel in the icon before any atom transforms are done; i.e. if the icon were scaled up to 3 times its size using the transform var, then a 3×3 region of pixels would all have the same icon-x/y values. The lower left pixel of the icon is 1,1. The vis-x/y parameters are screen-based, and their origin (1,1) is wherever the lower left corner of the icon is rendered.

Note: vis-x/y will not be included in the parameters if they are the same as icon-x/y.

If the mouse is over an overlay, icon-x/y and vis-x/y are relative to the parent object, not the overlay icon itself, so it's possible to have value outside of the normal range of 1,1 to [width],[height].

The mouse pointer may be customized as well. The following variables all deal with the appearance of the pointer. They do not control what actions may be taken by the user, but they provide hints to the user about what actions may work.

When selecting a mouse pointer, you may provide your own custom icon or use one of the <a href="#/DM/mouse/pointers">built-in pointers</a>.


> [!TIP]
> Note: Older games compiled prior to BYOND 4.0 had a different format for the `MouseDown()` and `MouseUp()` procs. These used `icon_x` and `icon_y` as arguments, but `control` and `params` have replaced them.


> [!TIP]
> Note: Games compiled before version 514 did not have the `button` parameter, so they handled the `left`, `middle`, and `right` parameters differently. In old versions, only the button used in the action (left, middle, right) was included as a parameter; now all buttons being held or changed are included, and `button` is the mouse button that changed.
***