[]{#/addtext proc.md}    
## addtext proc    
**See also:**    
:   [+ operator]/operator/+    
<!-- -->    
**Format:**    
:   addtext(Arg1,Arg2,\...)    
<!-- -->    
**Returns:**    
:   A text string with the arguments concatenated.    
<!-- -->    
**Args:**    
:   Any number of text strings.    
This instruction returns text containing the first argument followed by    
the second, followed by the third, etc. The arguments may be constants    
or variables containing text.    
### Example:    
var/T T = \"1\" T = addtext(T,\"\*1 = \",T) // T = \"1\*1 = 1\" world    
\<\< \"The answer is: \[T\]\"    
This instruction exists primarily for backwards-compatibility. You can    
accomplish the same thing with the + operator or by using embedded    
expressions.  