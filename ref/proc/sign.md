## sign proc 
###### BYOND Version 516

**Format:**
+   sign(A)

**Returns:**
+   The sign of A

**Args:**
+   A: A number

Returns 1 if A is a positive number
Returns -1 if A is a negative number
Returns 0 if A is anything else
### Example:

```dm
usr << sign(20) // outputs 1
usr << sign(0)  // outputs 0
usr << sign(-3) // outputs -1
```

> [!TIP] 
> **See also:**
> +   [floor proc](/ref/proc/floor.md) 
> +   [floor proc](/ref/proc/ceil.md) 
> +   [round proc](/ref/proc/round.md) 
> +   [trunc proc](/ref/proc/trunc.md) 
> +   [fract proc](/ref/proc/fract.md) 