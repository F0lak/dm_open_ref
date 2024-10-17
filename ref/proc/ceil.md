## ceil proc 
###### BYOND Version 515

**Format:**
+   ceil(A)

**Returns:**
+   the ceiling of A

**Args:**
+   A: A number, pixloc, or vector.

Returns the ceiling of A (the largest integer greater than or
equal to A).
### Example:

```dm
usr << ceil(1.45) // outputs 2

usr << ceil(-1.45) // outputs -1
```

> [!TIP] 
> **See also:**
> +   [floor proc](/ref/proc/floor.md) 
> +   [round proc](/ref/proc/round.md) 
> +   [trunc proc](/ref/proc/trunc.md) 
> +   [fract proc](/ref/proc/fract.md) 
> +   [sign proc](/ref/proc/sign.md) 