[]{#/operator/%3f%2e toc="?."}    
## ?. operator {#operator byondver="512"}    
**See also:**    
:   [. operator](/ref/operator/%2e)    
:   [: operator](/ref/operator/:)    
:   [?: operator](/ref/operator/%3f:)    
:   [operators](/ref/operator)    
This is used to access the procs and vars of a prototyped object. It is    
just like the . operator, but if the object is null, the access does not    
happen and there will be no runtime error. (A runtime error can still    
happen if the object is valid but is a different type that doesn\'t have    
the property available.)    
When used in an expression to read a value or call a proc from a null    
object, the result of the expression is null. When used for assignment,    
the assignment will not happen, and the expression being assigned will    
not be evaluated, if the object is null.    
### Example:    
var/mob/M // M is null by default M?.name = \"futz\" // assignment is    
skipped because M is null world \<\< M?.name // M?.name reads as null    
because M is null M?.Move(loc) // call Move() mob proc; again nothing    
happens M = new M?.name = \"futz\" // assignment is made because M is    
valid now world \<\< M?.name // outputs \"futz\" M?.Move(loc) // call    
Move() mob proc for M    
When reading `A?.B`, it\'s roughly equivalent to `A && A.B` except that    
`A` is only evalulated once, even if it\'s a complex expression like a    
proc call. Making an assignment to `A?.B` is the same: A is evalulated    
only once, and if it\'s not null then an assignment is made to its B    
var.    
For a version of this operator that doesn\'t check at compile time if    
the property is available, use the ?: operator instead.    
If ?. is used after a proc call, a list lookup, or a complex expression    
where the type can\'t be known, it will act like ?: instead.  