## grid control (skin)


A grid that contains multiple cells that can show various kinds
of output data.
**Grid-specific parameters:**
+   [cell-span](/ref/skin/param/cell-span.md) 
+   [cells](/ref/skin/param/cells.md) 
+   [current-cell](/ref/skin/param/current-cell.md) 
+   [enable-http-images](/ref/skin/param/enable-http-images.md) 
+   [highlight-color](/ref/skin/param/highlight-color.md) 
+   [is-list](/ref/skin/param/is-list.md) 
+   [line-color](/ref/skin/param/line-color.md) 
+   [link-color](/ref/skin/param/link-color.md) 
+   [show-lines](/ref/skin/param/show-lines.md) 
+   [show-names](/ref/skin/param/show-names.md) 
+   [small-icons](/ref/skin/param/small-icons.md) 
+   [style](/ref/skin/param/style.md) 
+   [visited-color](/ref/skin/param/visited-color.md) 


Sending output to a grid looks like this:
### Example:

``` dm
 // output to column 3, row 2 winset(usr, \"thegrid\",
\"current-cell=3,2\") usr \<\< output(\"Text\", \"thegrid\") // or even
easier: usr \<\< output(\"Text\", \"thegrid:3,2\") // when is-list is
true: usr \<\< output(\"5th item\", \"thegrid:5\") 
```



You can output an atom to the grid, which can be clicked,
dragged, etc. However, you should make sure that atom is *not* temporary
and will persist until you no longer need it, or else the server may
recycle it and the object in the cell will either disappear or be
impossible to interact with anymore. 

There are some limitations
to output in grid controls:
-   Only one character style (font, color, bold, etc.) may appear within
    a single cell.
-   A cell is either a link, or not.
-   One image is allowed per cell.
-   A cell can hold an object (atom), sent to it via the [`output()`
    proc](/ref/proc/output.md)  which can be clicked, dragged, etc.; it will
    not act as a link.
-   The same margin is used all around the cell, not different margins
    for left, right, top, bottom.
-   There will always be a 1-pixel space for grid lines, whether
    they\'re shown or not.