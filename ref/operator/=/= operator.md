[]{#/operator/=}    
## = operator    
**See also:**    
:   [\*= operator](/ref/operator/*=.md)    
:   [+= operator](/ref/operator/+=.md)    
:   [-= operator](/ref/operator/-=.md)    
:   [/= operator](/ref/operator//=.md)    
:   [%= operator](/ref/operator/%=.md)    
:   [\|= operator](/ref/operator/%7C=.md)    
:   [&= operator](/ref/operator/&=.md)    
:   [\^= operator](/ref/operator/%5E=.md)    
:   [\<\<= operator](/ref/operator/%3c%3c=.md)    
:   [\>\>= operator](/ref/operator/%3e%3e=.md)    
:   [:= operator](/ref/operator/:=.md)    
:   [\|\|= operator](/ref/operator/%7C%7C=.md)    
:   [&&= operator](/ref/operator/&&=.md)    
:   [operators](/ref/operator.md)    
<!-- -->    
**Format:**    
:   A = B    
Set A equal to B.    
Note that this is not the same as the equality test (==), which tests if    
A is equal to B.    
All assignment operators, including calculate-and-assign (such as the +=    
operator), can be chained together, and they are evaluated in    
right-to-left order. Therefore, a = b += c is a legal statement. It is    
equivalent to adding b and c, storing the result in b, then setting a to    
use the new value of b. (a = b) += c will, on the other hand, set a to    
equal b, then add c to a and store the result in a; b is never changed.  