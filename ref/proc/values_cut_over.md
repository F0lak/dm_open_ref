
## values_cut_over (proc)

**Format:**
+   values_cut_over(Alist, Max, inclusive=0)

**Arguments:**
+   Alist: An  or [list associations](/ref/list/associations)
+   Max: The maximum number allowed
+   inclusive: Also cut items whose value equals Max

**Returns:**
+   Number of items removed
***
Removes all items from the list whose associated values are greater than Max, not numbers, or <a href="#/proc/isnan">NaN</a>.

If the optional `inclusive` argument is true, items with associated values equal to Max are removed also.


```dm

var/list/stuff = list("a"=1, "b"=2, "c"=-4)
values_cut_over(stuff, 0)
for(var/k,v in stuff)
    usr << "[k] = [v]"
// prints:
// c = -4

```


This is a convenience proc for games trying to eke out high performance.

If Alist is not an associative list, nothing happens.
***
**Related Pages:**
+    [list associations](/ref/list/associations)
+    [values_cut_under proc](/ref/proc/values_cut_under)
