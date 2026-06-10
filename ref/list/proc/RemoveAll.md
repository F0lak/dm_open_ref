
## RemoveAll (proc)

**Format:**
+   list.RemoveAll(Item1,Item2,...)

**Arguments:**
+   One or more items to remove entirely from the list.

**Returns:**
+   Number of items removed.
***
Removes all copies of the specified items from the list. If an argument is itself a list, each item contained in it will be removed.

This is basically a faster version of the statement `while(list.Remove(Item1,Item2,...))` with an empty code block. For large lists this might be a big improvement because the list doesn't have to be traversed every time.
***
**Related Pages:**
+    [Add proc (list)](/ref/list/proc/Add)
+    [Remove proc (list)](/ref/list/proc/Remove)
