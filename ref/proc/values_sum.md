
## values_sum (proc)

**Format:**
+   values_sum(Alist)

**Arguments:**
+   Alist: An  or [list associations](/ref/list/associations)

**Returns:**
+   The sum of all associated numbers in Alist
***
Returns the sum of all associated values in this list that are numbers. Other values, including <a href="#/vector">vectors</a>, are not summed.


```dm

var/list/weights = list(/obj/crate = 12, /obj/vase = 1)
usr << values_sum(weights)  // outputs 13

```


This is a convenience proc for games trying to eke out high performance.

If Alist is not an associative list, the result is 0.
***
**Related Pages:**
+    [list associations](/ref/list/associations)
+    [values_product proc](/ref/proc/values_product)
+    [values_dot proc](/ref/proc/values_dot)
+    [values_cut_over proc](/ref/proc/values_cut_over)
+    [values_cut_under proc](/ref/proc/values_cut_under)
+    [alist proc](/ref/proc/alist)
