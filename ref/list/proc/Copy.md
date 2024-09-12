## Copy proc (list)
**See also:**
*   [Cut proc (list)](/ref/list/proc/Cut.md) <!-- -->
**Format:**
*   list.Copy(Start=1,End=0)
<!-- -->
**Returns:**
*   A new list.
<!-- -->
**Args:**
*   Start* The list position in which to begin the copy.
*   End* The list position immediately following the last element to be
    copied.


Copy list\[Start\] through list\[End-1\] into a new list. The
default end position of 0 stands for the position immediately after the
end of the list, so by default the entire list is copied.