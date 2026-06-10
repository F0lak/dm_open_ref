
## text2path (proc)

**Format:**
+   text2path(T)

**Arguments:**
+   T: A text string.

**Returns:**
+   a type path or null.
***

```dm

var/myturf = text2path("/turf/[src.color]")
if(myturf)
  src.loc = locate(myturf)

```


T is changed from a text string to the equivalent type path, or null if there is no such type.
***
**Related Pages:**
+    [ispath proc](/ref/proc/ispath)
