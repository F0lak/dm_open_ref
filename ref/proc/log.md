[]{#/log proc.md}    
## log proc    
**See also:**    
:   [\*\* operator](/operator/**)    
<!-- -->    
**Format:**    
:   log(X,Y)    
:   log(Y)    
<!-- -->    
**Returns:**    
:   The logarithm (base X) of Y. If X is not specified, a natural    
    logarithm is computed (base 2.718\...).    
The logarithm is the power to which you have to raise X in order to get    
Y. In other words, the following is true (ignoring round-off error): X    
\*\* log(X,Y) == Y    
One nice property of this function is that it gradually increases, with    
a slope that continuously tapers off. In other words, it can be useful    
to represent diminishing returns from some input, such as money,    
experience points, and so forth.  