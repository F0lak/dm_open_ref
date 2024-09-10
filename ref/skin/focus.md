## focus parameter (skin)    
**See also:**    
:   [id parameter](/%7Bskin%7D/param/id)    
:   [winget proc](/proc/winget)    
<!-- -->    
**Applies to:**    
:   [All](/%7Bskin%7D/control)    
<!-- -->    
**Format:**    
:   true/false    
<!-- -->    
**Default value:**    
:   false    
This parameter is true if this control currently has focus.    
This is also a special read-only global parameter. Calling    
[winget()](/proc/winget){.code} with no `id` and `focus` as the    
parameter will return the [id](/%7Bskin%7D/param/id){.code} of the    
currently focused control, if any.  