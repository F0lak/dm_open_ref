## max proc

**Format:**
+   max(A,B,C,\...)
<!-- -->
**Returns:**
+   the maximum of the arguments.
### Example:

``` dm
 usr \<\< max(1,2,3) 
```
 

This example
displays 3. 

If a single argument is specified, this is expected
to be a list and the maximum item from the list is returned.


Items to be compared may be numbers, text strings, pixlocs, or
vectors, or null, but different types may not be mixed. (Null values can
be mixed with nums or text, but that\'s the only exception.) 

If
the compared items are objects such as pixlocs or vectors, the result is
a new object, not one of the objects that was compared.

> [!TIP] 
> **See also:**
> +   [min proc](/ref/proc/min.md) 
> +   [clamp proc](/ref/proc/clamp.md) <!-- -->