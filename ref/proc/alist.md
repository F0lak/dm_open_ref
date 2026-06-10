
## alist (proc)

**Format:**
+   alist(A=a,B=b,C=c,...)

**Arguments:**
+   Arbitrary number of elements to be inserted into the associative list.

**Returns:**
+   A new associative list with contents (keys) A, B, C, and associated values a, b, c.
***
Creates a strictly associative list with key,value pairs. This is different from an <a href="#/list">ordinary list</a> in several respects.

The point of using this type over a regular list is to eke out performance gains in tight code. Operators such as `+` and `-` have improved performance because of the rules above.

In this proc the index values should be constants, and that usually means text constants. When these index values happen to be text strings that satisfy all the requirements for variable names, this may also be written in a convenient short-hand without the double quotes:


```dm

var/alist/lst = alist(player = "James Byond", score = 2000)

```


In other words, this is exactly the same syntax as for <a href="#/proc/arguments/named">named arguments</a>.
***
**Related Pages:**
+    [list associations](/ref/list/associations)
+    [list](/ref/list)
+    [list proc](/ref/proc/list)
+    [values_sum proc](/ref/proc/values_sum)
+    [values_product proc](/ref/proc/values_product)
+    [values_dot proc](/ref/proc/values_dot)
+    [values_cut_over proc](/ref/proc/values_cut_over)
+    [values_cut_under proc](/ref/proc/values_cut_under)
