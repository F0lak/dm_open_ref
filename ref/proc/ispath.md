## ispath proc

**Format:**
+   ispath(Val)
+   ispath(Val,Type)

**Returns:**
+   single-argument: 1 if Val is a type path
+   double-argument: 1 if Val is a type path derived from Type; 0
    otherwise.

**Args:**
+   Val: A type path.
+   Type: A type path or instance.
### Example:

```dm
var/M
M = /mob/ugly/duckling
if(ispath(M,/mob/ugly))  //true
if(ispath(M))            //true
if(ispath(new/mob))      //false
```

> [!TIP] 
> **See also:**
> +   [typesof proc](/ref/proc/typesof.md) 