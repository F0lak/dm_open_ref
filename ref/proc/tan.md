## tan proc 
###### BYOND Version 513
**See also:**
*   [arctan proc](/ref/proc/arctan.md) -m
*   [cos proc](/ref/proc/cos.md) -m
*   [sin proc](/ref/proc/sin.md) -m
*   [turn proc](/ref/proc/turn.md) -m<!-- -->
**Format:**
*   tan(X)
<!-- -->
**Returns:**
*   The tangent of X, where X is in degrees.
### Example:

```
 mob/verb/test() usr \<\< tan(0) // 0 usr \<\< tan(45) // 1
usr \<\< tan(90) // infinity (or close enough) 
```
