[]{#/proc/while}    
## while proc    
**See also:**    
:   [break statement](ref/proc/break)    
:   [continue statement](ref/proc/continue)    
:   [do proc](ref/proc/do)    
:   [for loop proc](ref/proc/for/loop)    
<!-- -->    
**Format:**    
:   while(E) Statement    
If E is true (non-zero) execute Statement. Continue testing E and doing    
the while block until E becomes false (zero).    
Statement may be a block of code or a single statement.    
### Example:    
var/i = 3 while(i) world \<\< i\--    
This outputs: 3 2 1  