## astype proc
##### BYOND Version 516
**Format:**
+   astype(Val,Type)
+   astype(Val)

**Returns:**
+   Val if Val is derived from Type; null otherwise.

**Args:**
+   Val: An object instance.
+   Type: An object prototype or instance. If no type is specified, it
    will be implied (see below).
Forcibly casts an object to a type, returning null if it isn\'t
valid.

### Example:
```dm
astype(gift, /obj/potion)?.Drink()
```

Similarly to `istype()`, the type can be implied. The implied
type is determined as follows:
1.  If `astype()` is on the right-hand side of an assignment operation,
    the left-hand side\'s var type is the implied type, just like with
    the `new()` operator.
2.  Otherwise, the var type of the first argument is the implied type,
    just as it is in `istype()`.

### Example:
```dm
// if obstacle is of type /obj/box, it will be assigned to B; otherwise B is null
var/obj/box/B = astype(obstacle)
if(B?.closed) B.Open()

// B is assigned no matter what, but astype() will return null if it isn't an /obj/box
B = obstacle
if(astype(B)?.closed) B.Open()
```
> [!TIP] 
> **See also:**
> +   [astype proc](/ref/proc/istype.md)
> +   [\_\_IMPLIED_TYPE\_\_ macro](/ref/DM/preprocessor/__IMPLIED_TYPE__.md) 