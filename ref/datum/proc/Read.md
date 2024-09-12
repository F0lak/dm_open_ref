## Read proc (datum)
**See also:**
+   [\>\> operator (savefile)](/ref/savefile/operator/%3e%3e.md) 
+   [Write proc (datum)](/ref/datum/proc/Write.md) 
+   [tmp vars](/ref/var/tmp.md) <!-- -->
**Format:**
+   Read(savefile/F)
<!-- -->
**When:**
+   Called when the object is read from a save file.
<!-- -->
**Args:**
+   F: the save file being read
<!-- -->
**Default action:**
+   Read the value of each variable from a directory by the same name as
    the variable. Variables marked tmp, global, or const and variables
    for which there is no directory are skipped.