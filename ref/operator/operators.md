[]{#/operator}    
## operators    
**See also:**    
:   [operator overloading](ref/operator/overload)    
Operators are used extensively in DM to compute numerical values.    
The DM operators are:    
``` dmcode    
() . : / ::     // here . : / are path operators    
[] . :    
?[] ?. ?:    
~ ! - ++ -- * &     // unary operators (* and & here are pointer operators)    
**    
* / % %%    
+ -    
< <= > >= <=>    
<< >>    
== != <> ~= ~!    
&    
^    
|    
&&    
||    
?               // ternary a ? b : c    
= += -= -= *= /= %= %%= &= |= ^= <<= >>= := &&= ||=    
in    
```    
Each line has higher order of operations than the next. Operators within    
a line have equal precedence and therefore are processed from left to    
right as they occur in an expression. (Assignment, or    
operate-and-assign, are processed from right to left.)    
Expressions of the form `A #= B` are shorthand for `A = A # B` except    
for `~=` and `:=`.    
### Example:    
var/N N = 0 // 0 N += 1+1\*2 // 3 if(1 + 1 == 2) N = 2 // 2 if(N==2 &&    
1/2==0.5) N = 0.5 // 0.5  