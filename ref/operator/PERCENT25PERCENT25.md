## %% operator {#operator byondver="515"}    
**See also:**    
:   [% operator](/operator/%)    
:   [%%= operator](/PERCENTPERCENT operator.md=)    
:   [operators](/operator)    
<!-- -->    
**Format:**    
:   A %% B    
<!-- -->    
**Returns:**    
:   The remainder of A / B.    
`A %% B` is read \"A modulo B\", which stands for the remainder of A    
divided by B.    
This is a newer version of the `%` operator that supports all numbers,    
not just integers. It is equivalent to `B * fract(A / B)`. The `%`    
operator does the same thing, but truncates A and B to integers first.    
A can be a vector instead of a number; B can also be a vector in this    
case.    
If A is a pixloc, it\'s treated like a 2D vector and the modulo    
operation is done with that instead.  