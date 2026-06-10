
## values_cut_under (proc)

**Format:**
+   values_cut_under(Alist, Min, inclusive=0)

**Arguments:**
+   Alist: An  or [list associations](/ref/list/associations)
+   Min: The maximum number allowed
+   inclusive: Also cut items whose value equals Min

**Returns:**
+   Number of items removed
***
Removes all items from the list whose associated values are less than Min, not numbers, or <a href="#/proc/isnan">NaN</a>.

If the optional `inclusive` argument is true, items with associated values equal to Min are removed also.


```dm

var/list/stuff = list("a"=1, "b"=2, "c"=-4)
values_cut_under(stuff, 0)
for(var/k,v in stuff)
    usr << "[k] = [v]"
// prints:
// a = 1
// b = 2

```


This is a convenience proc for games trying to eke out high performance.

If Alist is not an associative list, nothing happens.
***
**Related Pages:**
+    [list associations](/ref/list/associations)
+    [values_cut_over proc](/ref/proc/values_cut_over)
