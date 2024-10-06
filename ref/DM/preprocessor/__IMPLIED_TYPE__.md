## \_\_IMPLIED_TYPE\_\_ macro 
###### BYOND Version 515



The `__IMPLIED_TYPE__` macro is replaced by a reference to the
type path implied at the current point in compilation. For instance,
when using the [`new` proc](/ref/proc/new.md)  and assigning to a var, the type
path for `new()` is implied by the var\'s type. Implied types are also
automatically used in [locate()](/ref/proc/locate.md) , and are used by
default for the second argument in [istype()](/ref/proc/istype.md) .
### Example:

```dm
proc/Factory(new_type)
    world.log << "Creating new [new_type]"
    return new new_type()

proc/CreateThing()
    // pass /thing to Factory
    var/thing/T = Factory(__IMPLIED_TYPE__)
```

`__IMPLIED_TYPE__` is valid in the following situations:
-   In an expression on the right-hand side of an assignment operator
    (this includes operators like `+=`), where the left-hand side is a
    var that has a defined type path.
-   Within the second argument of [istype()](/ref/proc/istype.md) and [astype proc](/ref/proc/astype.md).

This is actually a pseudo-macro; the preprocessor doesn\'t
handle it directly.

> [!TIP] 
> **See also:**
> +   [\_\_FILE\_\_ macro](/ref/DM/preprocessor/__FILE__.md) 
> +   [\_\_LINE\_\_ macro](/ref/DM/preprocessor/__LINE__.md) 
> +   [\_\_PROC\_\_ macro](/ref/DM/preprocessor/__PROC__.md) 
> +   [\_\_TYPE\_\_ macro](/ref/DM/preprocessor/__TYPE__.md) 
> +   [new proc](/ref/proc/new.md) 
> +   [locate proc](/ref/proc/locate.md) 
> +   [istype proc](/ref/proc/istype.md) 
> +   [astype proc](/ref/proc/astype.md) 