## Error proc (world) 
###### BYOND Version 508

**Format:**
+   Error(exception)

**Args:**
+   exception: The error that was thrown. If this was a runtime error,
    the value will be an /exception datum.


Called when a runtime error happens, or the throw keyword is
used, without a try/catch to handle it. The return value is ignored.

> [!TIP] 
> **See also:**
> +   [try and catch statements](/ref/proc/try.md) 
> +   [throw statement](/ref/proc/throw.md) 
> +   [exception](/ref/exception.md) 