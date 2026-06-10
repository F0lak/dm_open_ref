
## Swap (proc)

**Format:**
+   list.Swap(Index1,Index2)

**Arguments:**
+   Index1: The index (1 to list.len) of one of the items to swap.
+   Index2: The index of the other item.

**Returns:**
+   Nothing.
***
Swap two items in a list. If the list has associated values, they will be preserved. This is most useful for user-defined sorting routines.


```dm

var/item
var/list/L = list("orange" = 3, "green" = 2, "blue" = 5)
for(item in L) world << "[item] -> [L[item]]"
world << ""
L.Swap(1, 3)
for(item in L) world << "[item] -> [L[item]]"

```



```dm

orange -> 3
green -> 2
blue -> 5

blue -> 5
green -> 2
orange -> 3

```


Note: This proc doesn't work with many special lists such as <code>contents</code> or <code>overlays</code>.
***
**Related Pages:**
+    [Cut proc (list)](/ref/list/proc/Cut)
+    [Copy proc (list)](/ref/list/proc/Copy)
+    [Insert proc (list)](/ref/list/proc/Insert)
