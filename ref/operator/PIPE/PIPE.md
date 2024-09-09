[]{#/operator/|}    
## \| operator    
**See also:**    
:   [& operator](ref/operator/&)    
:   [operators](ref/operator)    
:   [\|= operator](ref/operator/%7C=)    
<!-- -->    
**Format:**    
:   A \| B    
<!-- -->    
**Returns:**    
:   The binary \"or\" of A and B.    
A and B must be between 0 and 2\*\*24 - 1, giving an effective width of    
24 bits.    
If A and B are lists, the result is a list containing items that are in    
either list. list(1,2) \| list(2,3) is equivalent to list(1,2,3). The    
items from A come first in the result, followed by any extra items from    
B.    
If A is an icon or /icon datum, it is blended with B which can be either    
a color or another icon. Unlike the + or & operation, the result is    
transparent only in places where both icons were transparent.  