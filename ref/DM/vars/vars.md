[]{#/DM/vars}    
## vars list var (global) {#vars-list-var-global byondver="512"}    
**See also:**    
:   [vars list var (datum)](/ref/datum/var/vars)    
This is a list of all global variables. The items in the list are the    
variable names. If the variable name is used as an index into the list,    
the value of that variable is accessed.    
### Example:    
mob/verb/dumpglobal() for(var/V in global.vars) usr \<\< \"\[V\] =    
\[global.vars\[V\]\]\"    
This example displays all global variables. The `global` keyword is used    
here to distinguish it from `src.vars`, which in this example would be    
the mob\'s vars.  