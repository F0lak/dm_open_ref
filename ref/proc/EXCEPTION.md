## EXCEPTION proc

**Format:**
+   EXCEPTION(value)
<!-- -->
**Args:**
+   value: A text string (such as an error message) or other value
    identifying the exception.


This is used to create an /exception datum, and is shorthand
for calling new/exception(value, \_\_FILE\_\_, \_\_LINE\_\_). The value
you provide will be in exception.name.

> [!TIP] 
> **See also:**
> +   [try and catch statements](/ref/proc/try.md) 
> +   [throw statement](/ref/proc/throw.md) 
> +   [exception](/ref/exception.md) 
> +   [stddef.dm file](/ref/appendix/stddef%2edm.md) <!-- -->