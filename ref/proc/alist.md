## alist proc {#alist-proc byondver="516"}    
**See also:**    
:   [list associations](/list/associations)    
:   [list](/list)    
:   [list proc](/proc/list)    
<!-- -->    
**Format:**    
:   alist(A=a,B=b,C=c,\...)    
<!-- -->    
**Returns:**    
:   A new associative list with contents (keys) A, B, C, and associated    
    values a, b, c.    
<!-- -->    
**Args:**    
:   Arbitrary number of elements to be inserted into the associative    
    list.    
Creates a strictly associative list with key,value pairs. This is    
different from an [ordinary list](/list) in several respects.    
-   \"Keys\" can be numbers. This means list items can\'t be accessed by    
    a numerical index.    
-   Keys can\'t be repeated in the list, and always have an associated    
    value (even if it\'s just null).    
-   The order of keys in the list is not under user control.    
The point of using this type over a regular list is to eke out    
performance gains in tight code. Operators such as `+` and `-` have    
improved performance because of the rules above.    
In this proc the index values should be constants, and that usually    
means text constants. When these index values happen to be text strings    
that satisfy all the requirements for variable names, this may also be    
written in a convenient short-hand without the double quotes:    
var/alist/lst = alist(player = \"James Byond\", score = 2000)    
In other words, this is exactly the same syntax as for [named    
arguments](/proc/arguments/named).  