
## astype (proc)

**Format:**
+   astype(Val,Type)
+   astype(Val)

**Arguments:**
+   Val:  An object instance.
+   Type: An object prototype or instance. If no type is specified, it will be implied (see below).

**Returns:**
+   Val if Val is derived from Type; null otherwise.
***
Forcibly casts an object to a type, returning null if it isn't valid.


```dm

astype(gift, /obj/potion)?.Drink()

```


Similarly to `istype()`, the type can be implied. The implied type is determined as follows:


```dm

// if obstacle is of type /obj/box, it will be assigned to B; otherwise B is null
var/obj/box/B = astype(obstacle)
if(B?.closed) B.Open()

// B is assigned no matter what, but astype() will return null if it isn't an /obj/box
B = obstacle
if(astype(B)?.closed) B.Open()

```

***
**Related Pages:**
+    [istype proc](/ref/proc/istype)
+    [__IMPLIED_TYPE__ macro](/ref/DM/preprocessor/__IMPLIED_TYPE__)
