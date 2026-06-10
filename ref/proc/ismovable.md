
## ismovable (proc)

**Format:**
+   ismovable(Loc1, Loc2 ...)

**Arguments:**
+   Any number of locations to test.

**Returns:**
+   1 if all args are valid objs or mobs; 0 otherwise
***
Movable atoms are either objs or mobs, so this combines the `isobj` and `ismob` tests into a single proc.
***
**Related Pages:**
+    [isloc proc](/ref/proc/isloc)
+    [isobj proc](/ref/proc/isobj)
+    [ismob proc](/ref/proc/ismob)
