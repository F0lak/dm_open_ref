
## Join (proc)

**Format:**
+   list.Join(Glue,Start=1,End=0)

**Arguments:**
+   Glue: The text that will go between each item.
+   Start: The list item on which to begin.
+   End: The list item immediately following the last item to be joined.

**Returns:**
+   A text string made up of the items in this list, joined together by Glue.
***
This is exactly the same as calling jointext(List,Glue,Start,End), and is provided for convenience.
***
**Related Pages:**
+    [jointext proc](/ref/proc/jointext)
