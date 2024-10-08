## <=> operator 
###### BYOND Version 516

**Format:**
+   A <=> B

**Returns:**
+   -1 if A is less B; 1 if A is greater than B; 0 otherwise.


If A and B are text strings, a case sensitive comparison is
performed (like sorttextEx()). 

If either value is the special
number NaN (not a number), the result is currently 0 but should be
considered ambiguous.

> [!TIP] 
> **See also:**
> +   [< operator](/ref/operator/%3c.md) 
> +   [> operator](/ref/operator/%3e.md) 
> +   [<= operator](/ref/operator/%3c=.md) 
> +   [>= operator](/ref/operator/%3e=.md) 
> +   [== operator](/ref/operator/==.md) 
> +   [operators](/ref/operator.md) 
> +   [sorttextEx proc](/ref/proc/sorttextEx.md) 