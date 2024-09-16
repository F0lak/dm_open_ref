## ASSERT proc

**Format:**
+   ASSERT(expression)
<!-- -->
**Args:**
+   expression: an expression which should always be true


This is used to make a sanity check. If the given expression is
false, the current procedure crashes, generating diagnostic debugging
output, which includes the expression, a stack dump, and so forth.

> [!TIP] 
> **See also:**
> +   [CRASH proc](/ref/proc/CRASH.md) 
> +   [DEBUG definition](/ref/DM/preprocessor/define/DEBUG.md) 
> +   [stddef.dm file](/ref/appendix/stddef%2edm.md) <!-- -->