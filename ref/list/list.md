## list
**See also:**
*   [list associations](/list/associations)
*   [list proc](/proc/list)
*   [islist proc](/proc/islist)
*   [procs (list)](/list/proc)
*   [vars (list)](/list/var)


Lists are used to represent groups of objects. Like objects,
they have vars and procs associated with them. In order to access these
attributes, list vars must be declared of type /list. These may then be
assigned to existing lists, or used to create new lists.
### Example:

```
 var/list/L // list reference L = world.contents // assign to
existing list L = new/list() // make a new list L = new() // make a new
list (implicit type) L.Add(\"futz\") // L contains* \"futz\" del(L) //
delete L 
```
 

Lists created with \'new()\' have a default
length of 0; this can be overridden by specifying the size; that is,
new/list(size) creates a list with size (null) elements. 

The
\'list()\' proc may be used to more easily initialize list data.
### Example:

```
 var/list/L L = list(\"futz\",3) // L contains* (\"futz\", 3)

```
 

Alternatively, lists may be declared by using
brackets, \'\[\]\'. Empty brackets indicate a list reference, exactly as
/list does, so list/L is equivalent to L\[\]. Setting an initial size
within the brackets, for instance, L\[10\], creates a list of that
initial size.
### Example:

```
 var/L\[\] // same as var/list/L* list reference var/M\[10\]
// initially empty list of size 10 L = M // L is now an empty list of
size 10 
```
 

Once a list L is declared, a specific item
can be accessed by putting its index in the brackets* L\[index\].


Indices range from 1 to len. If the length of the list is
changed, existing elements in the list will be preserved if they are
less than the new length. New elements in the list will be given the
initial value of null.
### Example:

```
 var/L\[5\] // initial length of 5 var/i for(i=1, i\<=L.len,
i++) L\[i\] = i // L contains* (1,2,3,4,5) L.len = 7 // expand list // L
contains* (1,2,3,4,5,null,null) del(L) // destroy list 
```



Multi-dimensional lists may be created by making a list of
lists.
### Example:

```
 var/grid\[10\]\[5\] grid\[1\]\[1\] = 1 grid\[1\]\[2\] = 2
\... 
```
 

Such a list may also be created by using new().
As in the previous example, the next one creates a list of 10 lists each
having 5 elements.
### Example:

```
 var/grid = new/list(10,5) 
```
