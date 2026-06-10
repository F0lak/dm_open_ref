
## EXCEPTION (proc)

**Format:**
+   EXCEPTION(value)

**Arguments:**
+   value: A text string (such as an error message) or other value
identifying the exception.
***
This is used to create an /exception datum, and is shorthand for calling new/exception(value, __FILE__, __LINE__). The value you provide will be in exception.name.
***
**Related Pages:**
+    [try and catch statements](/ref/proc/try)
+    [throw statement](/ref/proc/throw)
+    [exception](/ref/exception)
+    [stddef.dm file](/ref/{{appendix}}/stddef%2edm)
