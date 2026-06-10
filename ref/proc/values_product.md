
## values_product (proc)

**Format:**
+   values_product(Alist)

**Arguments:**
+   Alist: An  or [list associations](/ref/list/associations)

**Returns:**
+   The product of all associated numbers in Alist, or 1 if no numbers were found
***
Returns the product of all associated values in this list that are numbers. Other values, including <a href="#/vector">vectors</a>, are not multiplied.


```dm

var/list/stuff = list("foo" = 3, "bar" = -4, "banana" = 5)
usr << values_product(stuff)  // outputs -60

```


This is a convenience proc for games trying to eke out high performance.

If Alist is not an associative list or no numbers were found among the associated values, the result is 1.
***
**Related Pages:**
+    [list associations](/ref/list/associations)
+    [values_sum proc](/ref/proc/values_sum)
+    [values_dot proc](/ref/proc/values_dot)
+    [values_cut_over proc](/ref/proc/values_cut_over)
+    [values_cut_under proc](/ref/proc/values_cut_under)
+    [alist proc](/ref/proc/alist)
