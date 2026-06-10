
## values_dot (proc)

**Format:**
+   values_dot(A, B)

**Arguments:**
+   A, B: An  or [list associations](/ref/list/associations)

**Returns:**
+   The dot product of all associated numbers in A and B
***
Returns the dot product of two associative lists. If the same item exists in both lists, the associated values are multiplied together as numbers. All of those multiplications are added together to form the dot product. This is similar to <a href="#/vector/proc/Dot">vector dot products</a>.


```dm

var/list/first = list("a"=1, "b"=2, "c"=3)
var/list/second = list("b"=4, "c"=5, "d"=6)
// first["a"] * second["a"] = 1 * 0 = 0
// first["b"] * second["b"] = 2 * 4 = 8
// first["c"] * second["c"] = 3 * 5 = 15
// first["d"] * second["d"] = 0 * 6 = 0
// total is 23
usr << values_dot(first, second)  // outputs 23

```


This is a convenience proc for games trying to eke out high performance.
***
**Related Pages:**
+    [list associations](/ref/list/associations)
+    [values_sum proc](/ref/proc/values_sum)
+    [values_product proc](/ref/proc/values_product)
+    [values_cut_over proc](/ref/proc/values_cut_over)
+    [values_cut_under proc](/ref/proc/values_cut_under)
+    [alist proc](/ref/proc/alist)
