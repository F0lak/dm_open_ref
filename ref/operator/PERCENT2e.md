[]{#/operator/%2e toc="."}    
## . operator    
**See also:**    
:   [: operator](/ref/operator/:.md)    
:   [?. operator](/ref/operator/%3f%2e.md)    
:   [?: operator](/ref/operator/%3f:.md)    
:   [operators](/ref/operator.md)    
This is used to access the procs and vars of a prototyped object. The    
variable need not actually contain a value with the specified type, but    
must at least be a type with the specified variable or a runtime error    
will occur, causing the proc to crash.    
### Example:    
var/mob/M = new M.name = \"futz\" // assign \'name\' mob var M.Move(0)    
// call \'Move()\' mob proc    
This is the same as the `:` operator, except that the compiler checks to    
see if the var type has this property, and throws a compiler error if    
not. It is good practice to use the `.` operator whenever possible, so    
more potential problems can be caught during compilation.    
If `.` follows a proc call, a list lookup, or a complex expression where    
the type can\'t be known, it will act like `:` instead.  