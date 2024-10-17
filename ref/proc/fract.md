## fract proc 
###### BYOND Version 515

**Format:**
+   fract(A)

**Returns:**
+   fractional part of A

**Args:**
+   A: A number, pixloc, or vector.

Returns the fractional part of the number A, with the same
sign. This is everything after the decimal point.
### Example:

```dm
usr << fract(1.45) // outputs 0.45

usr << fract(-1.45) // outputs -0.45
```
 
If A is a pixloc, it will be
treated as a vector with just its x and y parts, and the result will be
a vector.

> [!TIP] 
> **See also:**
> +   [trunc proc](/ref/proc/trunc.md) 
> +   [floor proc](/ref/proc/floor.md) 
> +   [ceil proc](/ref/proc/ceil.md) 
> +   [round proc](/ref/proc/round.md) 
> +   [sign proc](/ref/proc/sign.md) 