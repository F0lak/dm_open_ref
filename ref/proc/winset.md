
## winset (proc)

**Format:**
+   winset(player, control_id, params)

**Arguments:**
+   player: A mob or client.
+   control_id: The unique ID of a control in the player's skin.
+   params: A text string with parameters to set, in the format returned by
  ;  an associative list.
***
Sets parameters for a player's skin. The parameter list can be created by making a list and using `list2params()`, or it can be done manually by just using a string like `"is-visible=true;text-color=#f00"`. You can also just use a list directly, which will be passed to `list2params()` internally.

The `control_id` can be a window name, or in a `"[window].[control]"` format, or just the control ID as long as it is unique. In some special cases it can also be null. Another valid form is `":[type]"` which selects the default control of that type, e.g. `":map"` for the main map.

If you want to use a text string that may include spaces, surround the string with double quotes and escape them using a backslash, e.g. `"text=\"This is some text.\""`. Backslashes can also be used by preceding them with another backslash. For filenames, use single quotes around the file. Sometimes escapement may need to go several levels deep; for example to set up an input control with a default say command, you will need to escape it twice:

`winset(usr, "mainwindow.input", "command=**\"say \\\"\"**")`

You can set more than one control's parameters at once by leaving the `control_id` argument null, and including the control as part of the parameter list:


```dm
winset(usr, null,\
  "mainwindow.output.background-color=#ffffff;mainwindow.input.background-color=#ffffff")
```


Some "global" winset options will let you change things that affect the client as a whole, not just specific controls.

You can reset the skin to its beginning state, removing all runtime-created controls and windows, by calling `winset(player, null, "reset=true")`.

Another use for `winset()` is to send commands to the client that normally can only run from there, like `.profile` or `.quit`. To do this, leave the `control_id` argument null, and just use a parameter called "command":


```dm
obj/quitbutton
    name = "Quit"
    icon = 'buttons.dmi'
    icon_state = "quit"

    Click()
        winset(usr, null, list("command"=".quit"))
```


Because many characters need to be specially encoded for winsets, it's best to either use the list format of `winset()` which handles that encoding for you. If you want to use the string form, like `winset(usr, null, "command=XYZ")`, then you should use <a class="code" href="#/proc/url_encode">url_encode()</a> to encode your command.

The "browser-options" global parameter lets you enable or disable certain browser functionality. This can be a comma-separated list, or you can precede an option with `+` or `-` to enable or disable it specifically.
***
**Related Pages:**
+    [winclone proc](/ref/proc/winclone)
+    [winexists proc](/ref/proc/winexists)
+    [winget proc](/ref/proc/winget)
+    [winshow proc](/ref/proc/winshow)
+    [User interface skins](/ref/{skin})
+    [parameters](/ref/{skin}/param)
