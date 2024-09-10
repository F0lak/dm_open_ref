## ASSERT proc    
**See also:**    
:   [CRASH proc](/proc/CRASH)    
:   [DEBUG definition](/DM/preprocessor/define/DEBUG)    
:   [stddef.dm file](/%7B%7Bappendix%7D%7D/stddef%2edm)    
<!-- -->    
**Format:**    
:   ASSERT(expression)    
<!-- -->    
**Args:**    
:   expression: an expression which should always be true    
This is used to make a sanity check. If the given expression is false,    
the current procedure crashes, generating diagnostic debugging output,    
which includes the expression, a stack dump, and so forth.  