## oview proc    
**See also:**    
:   [\<\< output operator](/operator/%3c%3c/output)    
:   [orange proc](/proc/orange)    
:   [view proc](/proc/view)    
<!-- -->    
**Format:**    
:   oview(Dist,Center=usr)    
<!-- -->    
**Returns:**    
:   A list of visible objects within Dist tiles of Center, excluding    
    Center.    
<!-- -->    
**Args:**    
:   Dist: A number.    
:   Center: An object on the map.    
This instruction is just like view() except it doesn\'t include Center    
or its contents in the list.    
### Example:    
oview() \<\< \"to others in sight of \[usr\]\"  