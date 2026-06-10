
## id (info)
***
The name of this control. Read-only.

If this is a <a href="#/{skin}/control/main">Main control</a>, the name should always be unique. For others, it is usually still a good idea to use a unique name, but they can be referenced by *window*.*id* at runtime.

You can use a colon in front of the <a class="code" href="#/{skin}/param/type">type</a> to refer to the default control of a certain type, if one exists, e.g. `:map` is the default map.
***