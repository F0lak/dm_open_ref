[]{#/proc/issaved}    
## issaved proc    
**See also:**    
:   [initial proc](ref/proc/initial)    
:   [savefile](ref/savefile)    
:   [tmp vars](ref/var/tmp)    
:   [vars list var (datum)](ref/datum/var/vars)    
<!-- -->    
**Format:**    
:   issaved(Var)    
<!-- -->    
**Args:**    
:   Var: The variable to test.    
This returns 1 if the given variable should be automatically saved when    
writing an object to a savefile and 0 otherwise. Variables which are not    
global, const, or tmp will return 1.  