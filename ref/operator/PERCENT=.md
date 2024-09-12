## %= operator

**Format:**
+   A %= B


Set A equal to `A % B`. It is shorthand for `A = A % B`.


`A % B` is read \"A modulo B\", which stands for the remainder
of A divided by B. A and B are truncated to integers before the modulo;
use `%%=` instead to work with fractional values. 

If A is a
vector, it will be modified by this operation.

> [!TIP] 
> **See also:**
> +   [% operator](/ref/operator/%.md) 
> +   [operators](/ref/operator.md) <!-- -->