## list proc
**See also:**
*   [arglist proc](/ref/proc/arglist.md) -m
*   [list](/ref/list.md) -m
*   [list associations](/ref/list/associations.md) -m
<!-- -->
**Format:**
*   list(A,B,C,\...)
*   or
*   list(A=a,B=b,C=c,\...)
<!-- -->
**Returns:**
*   A new list with contents A, B, C, and (optional) associated values
    a, b, c.
<!-- -->
**Args:**
*   Arbitrary number of elements to be inserted into the list.


Assign elements to a list.
### Example:

```
 var/L\[\] L = list(1,2,3) 
```
 

This creates a
new list \'L\' that initially contains elements 1, 2, and 3. The length
of L is 3. 

The `list()` instruction may also be used to create
associative lists.
### Example:

```
 var/list/lst = list(\"player\" = \"James Byond\", \"score\" =
2000) 
```
 

That creates a list with contents (\"player,
\"score\") and associated values (\"James Byond\", 2000) respectively.


The index values should be constants, and that usually means
text constants. When these index values happen to be text strings that
satisfy all the requirements for variable names, this may also be
written in a convenient short-hand without the double quotes* 
```

var/list/lst = list(player = \"James Byond\", score = 2000) 
```



In other words, this is exactly the same syntax as for [named
arguments](/ref/proc/arguments/named.md) -m