## trunc proc 
###### BYOND Version 515

**Format:**
+   trunc(A)
<!-- -->
**Returns:**
+   truncated A
<!-- -->
**Args:**
+   A: A number, pixloc, or vector.


Returns the integer part of the number A. That is, this rounds
toward 0 to an integer.
### Example:

```
 usr \<\< trunc(1.45) // outputs 1 usr \<\< trunc(-1.45) //
outputs -1 
```


> [!TIP] 
> **See also:**
> +   [fract proc](/ref/proc/fract.md) 
> +   [floor proc](/ref/proc/floor.md) 
> +   [ceil proc](/ref/proc/ceil.md) 
> +   [round proc](/ref/proc/round.md) <!-- -->