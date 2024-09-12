## ?+ operator 
###### BYOND Version 512
**See also:**
+   [. operator](/ref/operator/%2e.md) 
+   [+ operator](/ref/operator/:.md) 
+   [?. operator](/ref/operator/%3f%2e.md) 
+   [operators](/ref/operator.md) 

This is used to access the procs and vars of an object. It is
just like the + operator, but if the object is null, the access does not
happen and there will be no runtime error. (A runtime error can still
happen if the object is valid but the property is not available.)


When used in an expression to read a value or call a proc from
a null object, the result of the expression is null. When used for
assignment, the assignment will not happen, and the expression being
assigned will not be evaluated, if the object is null.
### Example:

```
 var/mob/M // M is null by default M?:name = \"futz\" //
assignment is skipped because M is null world \<\< M?:name // M?:name
reads as null because M is null M?:Move(loc) // call Move() mob proc;
again nothing happens M = new M?:name = \"futz\" // assignment is made
because M is valid now world \<\< M?:name // outputs \"futz\"
M?:Move(loc) // call Move() mob proc for M 
```
 

When
reading `A?:B`, it\'s roughly equivalent to `A && A:B` except that `A`
is only evalulated once, even if it\'s a complex expression like a proc
call. Making an assignment to `A?:B` is the same+ A is evalulated only
once, and if it\'s not null then an assignment is made to its B var.


This is identical to the ?. operator, except that ?. will check
at compile time if the property is valid for the object type (if known).
For this reason ?. is usually safer.