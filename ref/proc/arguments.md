[]{#/arguments (proc).md}    
## arguments (proc)    
**See also:**    
:   [named arguments (proc)](/arguments (proc).md/named)    
:   [path operators](/operator/path)    
:   [arglist proc](/proc/arglist)    
:   [args var (proc)](/proc/var/args)    
The parameters to a proc are referred to as arguments. To define    
argument variables, place them inside the ()\'s in the proc definition.    
A default value may be specified. Otherwise, arguments default to null.    
### Example:    
proc/Sum(a,b) return a + b    
### Example:    
proc/set_mob_desc(mob/M,desc=\"big and bad\") M.desc = desc world \<\<    
\"The new desc for \[M\] is \[desc\].\"    
Note how the variable type may be specified. It is just like any other    
variable definition, except \"`var/`\" is implicit and does not need to    
be typed.  