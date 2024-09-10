[]{#/PIPEPIPE= operator.md}    
## \|\|= operator {#operator byondver="514"}    
**See also:**    
:   [\|\| operator](/operator/%7C%7C)    
:   [&& operator](/operator/&&)    
:   [&&= operator](/operator/&&=)    
:   [operators](/operator)    
<!-- -->    
**Format:**    
:   A \|\|= B    
<!-- -->    
**Returns:**    
:   Value of `(A || B)` after it has been assigned to A. This expression    
    can stand by itself; its result does not need to be assigned to    
    anything else.    
First A is evaluated. If its value is false, B will be evaluated and    
assigned to A. If A is true, B will not be evaluated and A will remain    
unchanged.    
Note that this is slightly different from `if(!A) A = B` if A is a    
complex expression such as `list[index++]`, because the expression is    
only evaluated once.    
This operator cannot be overloaded.  