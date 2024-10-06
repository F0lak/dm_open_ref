## output proc

<!-- -->
**Format:**
+   output(msg, control)
<!-- -->
**Args:**
+   msg: Text, an atom, a file, or null
+   control: The ID of a control in the player\'s skin, or null for the
    default


This is used in conjunction with the << output operator to
send output to a particular control in the player\'s skin. If null is
sent, the control will be cleared.
### Example:

```dm
 usr << output("Your score is [score].",
"scorepane.output") 
```
 

As with `winset()`, the
control name may be in the form `":[type]"` which sends to the default
control of that type, e.g. `":output"`. 

The control ID can be
followed by a colon and extra info such as a name or a grid cell, which
can send the output to the control in a different way. In a grid, this
can output directly to a specific grid cell, like so:
### Example:

```dm
 usr << output("Column 3, Row 2", "examplegrid:3,2")

```
 

For a browser control, the extra info is a
JavaScript function. The format for sending a script to the browser
control is `output("[params]","[control]:[scriptname]")` where
"[params]" is a URL-encoded list of string arguments to the
javascript function, as formatted by
[list2params()](/ref/proc/list2params.md).
### Example:

```dm
 mob/Login() . = ..() usr << output(\\ {"
::: 
###### BYOND Version  proc

<!-- -->
**Format:**
+   output(msg, control)
<!-- -->
**Args:**
+   msg: Text, an atom, a file, or null
+   control: The ID of a control in the player\'s skin, or null for the
    default


This is used in conjunction with the << output operator to
send output to a particular control in the player\'s skin. If null is
sent, the control will be cleared.
### Example:

```dm
 usr << output("Your score is [score].",
"scorepane.output") 
```
 

As with `winset()`, the
control name may be in the form `":[type]"` which sends to the default
control of that type, e.g. `":output"`. 

The control ID can be
followed by a colon and extra info such as a name or a grid cell, which
can send the output to the control in a different way. In a grid, this
can output directly to a specific grid cell, like so:
### Example:

```dm
 usr << output("Column 3, Row 2", "examplegrid:3,2")

```
 

For a browser control, the extra info is a
JavaScript function. The format for sending a script to the browser
control is `output("[params]","[control]:[scriptname]")` where
"[params]" is a URL-encoded list of string arguments to the
javascript function, as formatted by
[list2params()](/ref/proc/list2params.md).
### Example:

```dm
 mob/Login() . = ..() usr << output(\\ {"
::: {#foo}
This text can change.
:::


And this can\'t.
\, ":browser"); #define LP(str) list2params(list(str))
mob/verb/newtext(T as text) usr << output(LP(T), ":browser:replace")

```
 

This allows for the creation of more dynamic
interfaces, since javascript provides access to many client-side
operations and flicker-free updates.

> [!TIP] 
> **See also:**
> +   [<< output operator](/ref/operator/%3c%3c/output.md) 
> +   [winclone proc](/ref/proc/winclone.md) 
> +   [winset proc](/ref/proc/winset.md) 