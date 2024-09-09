[]{#/proc/min}    
## min proc    
**See also:**    
:   [max proc](ref/proc/max)    
:   [clamp proc](ref/proc/clamp)    
<!-- -->    
**Format:**    
:   min(A,B,C,\...)    
<!-- -->    
**Returns:**    
:   the minimum of the arguments.    
### Example:    
usr \<\< min(1,2,3)    
This example displays 1.    
If a single argument is specified, this is expected to be a list and the    
minimum item from the list is returned.    
Items to be compared may be numbers, text strings, pixlocs, or vectors,    
or null, but different types may not be mixed. (Null values can be mixed    
with nums or text, but that\'s the only exception.)    
If the compared items are objects such as pixlocs or vectors, the result    
is a new object, not one of the objects that was compared.  