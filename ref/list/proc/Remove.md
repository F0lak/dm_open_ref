
## Remove (proc)

**Format:**
+   list.Remove(Item1,Item2,...)

**Arguments:**
+   One or more items to remove from the list.

**Returns:**
+   1 if any items removed, 0 if not.
***
Removes the specified items from the list. If an argument is itself a list, each item contained in it will be removed. Removal starts at the end of the list (highest index) so that this operation is an exact reversal of Add().
***
**Related Pages:**
+    [- operator](/ref/operator/-)
+    [Add proc (list)](/ref/list/proc/Add)
+    [RemoveAll proc (list)](/ref/list/proc/RemoveAll)
