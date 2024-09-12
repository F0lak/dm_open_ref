## focus parameter (skin)
**See also:**
+   [id parameter](/ref/%7Bskin%7D/param/id.md) 
+   [winget proc](/ref/proc/winget.md) 
<!-- -->
**Applies to:**
+   [All](/ref/%7Bskin%7D/control.md) 
<!-- -->
**Format:**
+   true/false
<!-- -->
**Default value:**
+   false


This parameter is true if this control currently has focus.


This is also a special read-only global parameter. Calling
[winget()](/ref/proc/winget.md) {.code} with no `id` and `focus` as the
parameter will return the [id](/ref/%7Bskin%7D/param/id.md) of the
currently focused control, if any.