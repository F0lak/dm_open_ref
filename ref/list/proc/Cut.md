## Cut proc (list)
**See also:**
*   [Copy proc (list)](/ref/list/proc/Copy.md) 
*   [Insert proc (list)](/ref/list/proc/Insert.md) <!-- -->
**Format:**
*   list.Cut(Start=1,End=0)
<!-- -->
**Args:**
*   Start* The list position in which to begin the cut.
*   End* The list position immediately following the last element to be
    removed.


Remove the elements between list\[Start\] and list\[End-1\],
decreasing the size of the list appropriately. The default end position
of 0 stands for the position immediately after the end of the list, so
by default the entire list is deleted.