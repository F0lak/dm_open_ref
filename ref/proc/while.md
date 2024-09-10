[]{#/while proc.md}    
## while proc    
**See also:**    
:   [break statement](/proc/break)    
:   [continue statement](/proc/continue)    
:   [do proc](/proc/do)    
:   [for loop proc](/proc/for/loop)    
<!-- -->    
**Format:**    
:   while(E) Statement    
If E is true (non-zero) execute Statement. Continue testing E and doing    
the while block until E becomes false (zero).    
Statement may be a block of code or a single statement.    
### Example:    
var/i = 3 while(i) world \<\< i\--    
This outputs: 3 2 1  