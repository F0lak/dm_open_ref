
## vars (var)
***
This is a list of all the variables belonging to an object. The items in the list are the variable names. If the variable name is used as an index into the list, the value of that variable is accessed.


```dm

mob/verb/dump()
   var/V
   for(V in vars)
      usr << "[V] = [vars[V]]"

```


This example displays all the variables belonging to your mob.
***
**Related Pages:**
+    [initial proc](/ref/proc/initial)
+    [issaved proc](/ref/proc/issaved)
+    [list](/ref/list)
+    [list associations](/ref/list/associations)
+    [vars list var (global)](/ref/DM/vars)
