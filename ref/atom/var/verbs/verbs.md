[]{#/atom/var/verbs}    
## verbs list var (atom)    
**See also:**    
:   [list](/ref/list)    
:   [typesof proc](/ref/proc/typesof)    
<!-- -->    
**Default value:**    
:   The list of verbs defined for the object\'s prototype.    
This is a list of the object\'s verbs. Initially, it contains all of the    
verbs defined in the prototype. It may be used to add and remove verbs    
at runtime.    
Note that this variable is not automatically saved when the object is    
written to a savefile. That behavior may change in the future. In the    
mean time, you must save any necessary changes yourself or they will not    
be preserved when the object is loaded.    
### Example:    
mob/proc/kazaam() usr \<\< \"Kazaam!\" mob/verb/add_kazaam() verbs +=    
/mob/proc/kazaam mob/verb/remove_kazaam() verbs -= /mob/proc/kazaam  