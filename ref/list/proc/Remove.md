## Remove proc (list)
**See also:**
*   [- operator](/ref/operator/-.md) -m
*   [Add proc (list)](/ref/list/proc/Add.md) -m
*   [RemoveAll proc (list)](/ref/list/proc/RemoveAll.md) -m<!-- -->
**Format:**
*   list.Remove(Item1,Item2,\...)
<!-- -->
**Returns:**
*   1 if any items removed, 0 if not.
<!-- -->
**Args:**
*   One or more items to remove from the list.


Removes the specified items from the list. If an argument is
itself a list, each item contained in it will be removed. Removal starts
at the end of the list (highest index) so that this operation is an
exact reversal of Add().