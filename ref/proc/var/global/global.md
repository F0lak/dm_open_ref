[]{#/proc/var/global}    
## global var (proc)    
**See also:**    
:   [src var (proc)](ref/proc/var/src)    
This is not really a variable but is used to force treatment of the    
following variable or proc as global. This may be necessary if a local    
or src-level variable has the same name.    
### Example:    
var/myvar = \"global\" mob verb/test() var/myvar = \"local\" usr \<\<    
myvar usr \<\< global.myvar    
This example outputs \"local\" and then \"global\".  