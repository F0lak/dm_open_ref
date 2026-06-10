
## initial (proc)

**Format:**
+   initial(Var)

**Arguments:**
+   Var: A variable to find the initial value of.
***
This returns the original compile-time value of a variable. It could be used to reset a variable to its default value or to check if a variable has changed.


```dm

obj/verb/set_icon(I as null|icon)
   if(!I) I = initial(icon)
   icon = I

```

***
**Related Pages:**
+    [:: operator](/ref/operator/::)
+    [issaved proc](/ref/proc/issaved)
+    [vars](/ref/datum/var/vars)
