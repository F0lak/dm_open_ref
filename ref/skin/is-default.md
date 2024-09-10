## is-default parameter (skin)    
**See also:**    
:   [id parameter](/%7Bskin%7D/param/id)    
:   [parent parameter](/%7Bskin%7D/param/parent)    
:   [type parameter](/%7Bskin%7D/param/type)    
<!-- -->    
**Applies to:**    
:   [All](/%7Bskin%7D/control)    
<!-- -->    
**Format:**    
:   true/false    
<!-- -->    
**Default value:**    
:   false    
Specifies that this is a default control. This should be true for your    
main window, and for your primary map, info, output, input, and browser    
controls.    
The default control of a given type can be referenced in    
[winset()](/proc/winset){.code} and other skin-related procs by the    
name `":`*`type`*`"`, e.g. `":map"`.    
Changing this value at runtime should be avoided, especially for    
windows. Results may be unpredictable.  