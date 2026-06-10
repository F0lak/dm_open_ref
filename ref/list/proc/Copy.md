
## Copy (proc)

**Format:**
+   list.Copy(Start=1,End=0)

**Arguments:**
+   Start: The list position in which to begin the copy.
+   End: The list position immediately following the last element to be
     copied.

**Returns:**
+   A new list.
***
Copy list[Start] through list[End-1] into a new list. The default end position of 0 stands for the position immediately after the end of the list, so by default the entire list is copied.
***
**Related Pages:**
+    [Cut proc (list)](/ref/list/proc/Cut)
