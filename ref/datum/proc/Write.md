
## Write (proc)

**Format:**
+   Write(savefile/F)

**Arguments:**
+   F: the save file being written to

**Called When:**
+   Called when the object is written to a save file.

**Default Action:**
+   Write the value of each variable to a directory by the same name as the
    variable.  Variables marked tmp, global, or const and variables which
    are equal to their initial value are skipped.
******
**Related Pages:**
+    [<< operator (savefile)](/ref/savefile/operator/%3c%3c)
+    [Read](/ref/datum/proc/Read)
+    [initial proc](/ref/proc/initial)
+    [issaved proc](/ref/proc/issaved)
+    [tmp vars](/ref/var/tmp)
