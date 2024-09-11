## Find proc (list)
**Format:**
*   list.Find(Elem,Start=1,End=0)
<!-- -->
**Returns:**
*   The first position of elem in list, or 0 if not found.
<!-- -->
**Args:**
*   Elem* The element to find.
*   Start* The list position in which to begin the search.
*   End* The list position immediately following the end of the search.


Find the first position of Elem in the list. Elements between
Start and End are searched. The default end position of 0 stands for the
position immediately after the end of the list, so by default the entire
list is searched.