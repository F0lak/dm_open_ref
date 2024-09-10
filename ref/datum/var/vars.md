## vars list var (datum)    
**See also:**    
:   [initial proc](/proc/initial)    
:   [issaved proc](/proc/issaved)    
:   [list](/list)    
:   [list associations](/list/associations)    
:   [vars list var (global)](/DM/vars)    
This is a list of all the variables belonging to an object. The items in    
the list are the variable names. If the variable name is used as an    
index into the list, the value of that variable is accessed.    
### Example:    
mob/verb/dump() var/V for(V in vars) usr \<\< \"\[V\] = \[vars\[V\]\]\"    
This example displays all the variables belonging to your mob.  