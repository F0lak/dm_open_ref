[]{#/{skin}/param/id}
## id parameter (skin)
**See also:**
:   [parent parameter](#/%7Bskin%7D/param/parent)
:   [type parameter](#/%7Bskin%7D/param/type)
<!-- -->
**Applies to:**
:   [All](#/%7Bskin%7D/control)
<!-- -->
**Format:**
:   string
The name of this control. Read-only.
If this is a [Main control](#/%7Bskin%7D/control/main), the name should
always be unique. For others, it is usually still a good idea to use a
unique name, but they can be referenced by *window*.*id* at runtime.
You can use a colon in front of the
[type](#/%7Bskin%7D/param/type){.code} to refer to the default control
of a certain type, if one exists, e.g. `:map` is the default map.