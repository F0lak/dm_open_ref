## \_\_IMPLIED_TYPE\_\_ macro 
###### BYOND Version 515
**See also:**
*   [\_\_FILE\_\_ macro](/DM/preprocessor/__FILE__)
*   [\_\_LINE\_\_ macro](/DM/preprocessor/__LINE__)
*   [\_\_PROC\_\_ macro](/DM/preprocessor/__PROC__)
*   [\_\_TYPE\_\_ macro](/DM/preprocessor/__TYPE__)
*   [new proc](/proc/new)
*   [locate proc](/proc/locate)
*   [istype proc](/proc/istype)


The `__IMPLIED_TYPE__` macro is replaced by a reference to the
type path implied at the current point in compilation. For instance,
when using the [`new` proc](/proc/new) and assigning to a var, the type
path for `new()` is implied by the var\'s type. Implied types are also
automatically used in [`locate()`](/proc/locate), and are used by
default for the second argument in [`istype()`](/proc/istype).
### Example:

```
 proc/Factory(new_type) world.log \<\< \"Creating new
\[new_type\]\" return new new_type() proc/CreateThing() // pass /thing
to Factory var/thing/T = Factory(\_\_IMPLIED_TYPE\_\_) 
```



`__IMPLIED_TYPE__` is valid in the following situations:
-   In an expression on the right-hand side of an assignment operator
    (this includes operators like `+=`), where the left-hand side is a
    var that has a defined type path.
-   Within the second argument of [`istype()`](/proc/istype).


This is actually a pseudo-macro; the preprocessor doesn\'t
handle it directly.