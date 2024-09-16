## winget proc

<!-- -->
**Format:**
+   winget(player, control_id, params)
<!-- -->
**Args:**
+   player: A mob or client.
+   control_id: The unique ID of a control in the player\'s skin.
+   params: The name of a parameter to read, or a semicolon-separated
    list of parameters


Retrieves info from a player about the current state of their
skin. If `control_id` and `params` are each just a single value, then
the return value will be a simple string with the value of that
parameter. If `control_id` or `params` is a semicolon-separated list
like the kind used in `list2params()`, then the result will be in a
similar format, and can be converted to a list form using
`params2list()`. 

The `control_id` can be a window name, or in a
`"[window].[control]"` format, or just the control\'s ID itself as long
as it is unique. Another valid form is `":[type]"` which selects the
default control of that type, e.g. `":map"` for the main map. As
mentioned above, you can retrieve info on more than one control at once
by separating them with semicolons, like `"button1;button2"`.
### Example:

``` dm
 usr << "mainwindow.is-visible = [winget(usr,
"mainwindow", "is-visible")]" usr << "\\nOther params:" usr
<< winget(usr, "mainwindow", "pos;is-maximized") usr <<
"\\nButtons:" usr << winget(usr, "button1;button2",
"is-checked") 
```
 

This outputs: 
``` dm

mainwindow.is-visible = true Other params: pos=0x0;is-maximized=true
Buttons: button1.is-checked=true;button2.is-checked=false 
```



If the returned result is actual text for any parameters, the
single quote or double quote characters may be escaped with a backslash.
An actual backslash will also be escaped with a backslash. 

You
can also use a special wildcard format to retrieve info about all the
controls in a window, menu, or macro set. If control_id is
`"mainwindow.*"` for instance, then any control that is part of
`mainwindow`---and `mainwindow` itself---is included in the result if it
has the parameter(s) you\'re looking for. Use `params2list()` to
interpret the result.
Note: Because the client must be contacted to get this information,
`winget()` will sleep the current proc.
### Special wingets


Calling `winget()` with a blank or null `control_id` can return
some values that belong to the client as a whole, not to specific
controls. They can also be used for [embedded
wingets](/ref/skin/commands.md) 
focus
+   The full ID of the control, if any, that currently has keyboard
    focus.
windows
+   The IDs of all windows, separated by semicolons.
panes
+   The IDs of all panes, separated by semicolons.
menus
+   The IDs of all menus, separated by semicolons.
macros
+   The IDs of all macro sets, separated by semicolons.
sound
+   True if sounds are enabled.
hwmode
+   True if the map displays in hardware rendering mode.
url
+   The URL the client is connected to in `IP:port` form. The port is 0
    if connected to a local .dmb file, and either an empty string or
    null is returned if Dream Seeker is not connected at all.
num-lock
+   True if Num Lock is on.
caps-lock
+   True if Caps Lock is on.
scroll-lock
+   True if Scroll Lock is on.

> [!TIP] 
> **See also:**
> +   [winexists proc](/ref/proc/winexists.md) 
> +   [winset proc](/ref/proc/winset.md) 
> +   [User interface skins](/ref/skin.md) 
> +   [parameters (skin)](/ref/skin/param.md) 