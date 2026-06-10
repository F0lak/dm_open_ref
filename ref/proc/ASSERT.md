
## ASSERT (proc)

**Format:**
+   ASSERT(expression)

**Arguments:**
+   expression: an expression which should always be true
***
This is used to make a sanity check. If the given expression is false, the current procedure crashes, generating diagnostic debugging output, which includes the expression, a stack dump, and so forth.
***
**Related Pages:**
+    [CRASH proc](/ref/proc/CRASH)
+    [DEBUG definition](/ref/DM/preprocessor/define/DEBUG)
+    [stddef.dm file](/ref/{{appendix}}/stddef%2edm)
