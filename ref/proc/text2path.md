## text2path proc

**Format:**
+   text2path(T)

**Args:**
+   T: A text string.

**Returns:**
+   a type path or null.
### Example:

```dm
var/myturf = text2path("/turf/[src.color]")
if(myturf)
  src.loc = locate(myturf)
```
 
T is changed from a text
string to the equivalent type path, or null if there is no such type.

> [!TIP] 
> **See also:**
> +   [ispath proc](/ref/proc/ispath.md) 