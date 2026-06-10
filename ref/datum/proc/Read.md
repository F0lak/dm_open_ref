
## Read (proc)

**Format:**
+   Read(savefile/F)

**Arguments:**
+   F: the save file being read

**Called When:**
+   Called when the object is read from a save file.

**Default Action:**
+   Read the value of each variable from a directory by the same name as the
    variable.  Variables marked tmp, global, or const and variables for
    which there is no directory are skipped.
******
**Related Pages:**
+    [>> operator (savefile)](/ref/savefile/operator/%3e%3e)
+    [Write](/ref/datum/proc/Write)
+    [tmp vars](/ref/var/tmp)
