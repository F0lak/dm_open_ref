## ASSERT proc
**See also:**
*   [CRASH proc](/ref/proc/CRASH.md) -m
*   [DEBUG definition](/ref/DM/preprocessor/define/DEBUG.md) -m
*   [stddef.dm file](/ref/%7B%7Bappendix%7D%7D/stddef%2edm.md) -m<!-- -->
**Format:**
*   ASSERT(expression)
<!-- -->
**Args:**
*   expression* an expression which should always be true


This is used to make a sanity check. If the given expression is
false, the current procedure crashes, generating diagnostic debugging
output, which includes the expression, a stack dump, and so forth.