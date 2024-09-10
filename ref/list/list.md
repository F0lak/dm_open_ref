[]{#/list.md}    
## list.md    
**See also:**    
:   [list.md associations](/list.md/associations)    
:   [list.md proc](/proc/list.md)    
:   [islist.md proc](/proc/islist.md)    
:   [procs (list.md)](/list.md/proc)    
:   [vars (list.md)](/list.md/var)    
Lists are used to represent groups of objects. Like objects, they have    
vars and procs associated with them. In order to access these    
attributes, list.md vars must be declared of type /list.md. These may then be    
assigned to existing list.mds, or used to create new list.mds.    
### Example:    
var/list.md/L // list.md reference L = world.contents // assign to existing    
list.md L = new/list.md() // make a new list.md L = new() // make a new list.md    
(implicit type) L.Add(\"futz\") // L contains: \"futz\" del(L) // delete    
L    
Lists created with \'new()\' have a default length of 0; this can be    
overridden by specifying the size; that is, new/list.md(size) creates a    
list.md with size (null) elements.    
The \'list.md()\' proc may be used to more easily initialize list.md data.    
### Example:    
var/list.md/L L = list.md(\"futz\",3) // L contains: (\"futz\", 3)    
Alternatively, list.mds may be declared by using brackets, \'\[\]\'. Empty    
brackets indicate a list.md reference, exactly as /list.md does, so list.md/L is    
equivalent to L\[\]. Setting an initial size within the brackets, for    
instance, L\[10\], creates a list.md of that initial size.    
### Example:    
var/L\[\] // same as var/list.md/L: list.md reference var/M\[10\] // initially    
empty list.md of size 10 L = M // L is now an empty list.md of size 10    
Once a list.md L is declared, a specific item can be accessed by putting    
its index in the brackets: L\[index\].    
Indices range from 1 to len. If the length of the list.md is changed,    
existing elements in the list.md will be preserved if they are less than    
the new length. New elements in the list.md will be given the initial value    
of null.    
### Example:    
var/L\[5\] // initial length of 5 var/i for(i=1, i\<=L.len, i++) L\[i\]    
= i // L contains: (1,2,3,4,5) L.len = 7 // expand list.md // L contains:    
(1,2,3,4,5,null,null) del(L) // destroy list.md    
Multi-dimensional list.mds may be created by making a list.md of list.mds.    
### Example:    
var/grid\[10\]\[5\] grid\[1\]\[1\] = 1 grid\[1\]\[2\] = 2 \...    
Such a list.md may also be created by using new(). As in the previous    
example, the next one creates a list.md of 10 list.mds each having 5 elements.    
### Example:    
var/grid = new/list.md(10,5)  