## focus parameter (skin)
**See also:**
*   [id parameter](/ref/%7Bskin%7D/param/id.md) -m
*   [winget proc](/ref/proc/winget.md) -m
<!-- -->
**Applies to:**
*   [All](/ref/%7Bskin%7D/control.md) -m
<!-- -->
**Format:**
*   true/false
<!-- -->
**Default value:**
*   false


This parameter is true if this control currently has focus.


This is also a special read-only global parameter. Calling
[winget()](/ref/proc/winget.md) -m{.code} with no `id` and `focus` as the
parameter will return the [id](/ref/%7Bskin%7D/param/id.md) -m.code} of the
currently focused control, if any.