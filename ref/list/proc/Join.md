## Join proc (list) 
###### BYOND Version 510

**Format:**
+   list.Join(Glue,Start=1,End=0)

**Returns:**
+   A text string made up of the items in this list, joined together by
    Glue.

**Args:**
+   Glue: The text that will go between each item.
+   Start: The list item on which to begin.
+   End: The list item immediately following the last item to be joined.

This is exactly the same as calling
jointext(List,Glue,Start,End), and is provided for convenience.

> [!TIP] 
> **See also:**
> +   [jointext proc](/ref/proc/jointext.md) 