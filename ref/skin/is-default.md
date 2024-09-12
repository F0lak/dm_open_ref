## is-default parameter (skin)

<!-- -->
**Applies to:**
+   [All](/ref/%7Bskin%7D/control.md) 
<!-- -->
**Format:**
+   true/false
<!-- -->
**Default value:**
+   false


Specifies that this is a default control. This should be true
for your main window, and for your primary map, info, output, input, and
browser controls. 

The default control of a given type can be
referenced in [winset()](/ref/proc/winset.md) and other skin-related
procs by the name `":`*`type`*`"`, e.g. `":map"`. 

Changing this
value at runtime should be avoided, especially for windows. Results may
be unpredictable.

**See also:**
+   [id parameter](/ref/%7Bskin%7D/param/id.md) 
+   [parent parameter](/ref/%7Bskin%7D/param/parent.md) 
+   [type parameter](/ref/%7Bskin%7D/param/type.md) 