[]{#/proc/do}    
## do proc    
**See also:**    
:   [break statement](/ref/proc/break/break.md)    
:   [continue statement](/ref/proc/continue/continue.md)    
:   [for loop proc](/ref/proc/for/loop/loop.md)    
:   [while proc](/ref/proc/while/while.md)    
<!-- -->    
**Format:**    
:   do Statement while( E )    
Execute Statement. If E is true (non-zero) do it over again. Continue    
until E is false (zero).    
Statement may be a block of code or a single statement.    
### Example:    
var/i = 3 do world \<\< i\-- while(i)    
This outputs: 3 2 1  