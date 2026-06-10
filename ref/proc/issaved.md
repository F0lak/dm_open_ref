
## issaved (proc)

**Format:**
+   issaved(Var)

**Arguments:**
+   Var: The variable to test.
***
This returns 1 if the given variable should be automatically saved when writing an object to a savefile and 0 otherwise. Variables which are not global, const, or tmp will return 1.
***
**Related Pages:**
+    [initial proc](/ref/proc/initial)
+    [savefile](/ref/savefile)
+    [tmp vars](/ref/var/tmp)
+    [vars](/ref/datum/var/vars)
