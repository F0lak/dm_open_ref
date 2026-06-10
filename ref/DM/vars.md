
## vars (info)
***
This is a list of all global variables. The items in the list are the variable names. If the variable name is used as an index into the list, the value of that variable is accessed.


```dm

mob/verb/dumpglobal()
   for(var/V in global.vars)
      usr << "[V] = [global.vars[V]]"

```


This example displays all global variables. The <code>global</code> keyword is used here to distinguish it from <code>src.vars</code>, which in this example would be the mob's vars.
***
**Related Pages:**
+    [vars](/ref/datum/var/vars)
