## grid control (skin)


A grid that contains multiple cells that can show various kinds
of output data.
**Grid-specific parameters:**
*   [cell-span](/ref/%7Bskin%7D/param/cell-span.md) -m
*   [cells](/ref/%7Bskin%7D/param/cells.md) -m
*   [current-cell](/ref/%7Bskin%7D/param/current-cell.md) -m
*   [enable-http-images](/ref/%7Bskin%7D/param/enable-http-images.md) -m
*   [highlight-color](/ref/%7Bskin%7D/param/highlight-color.md) -m
*   [is-list](/ref/%7Bskin%7D/param/is-list.md) -m
*   [line-color](/ref/%7Bskin%7D/param/line-color.md) -m
*   [link-color](/ref/%7Bskin%7D/param/link-color.md) -m
*   [show-lines](/ref/%7Bskin%7D/param/show-lines.md) -m
*   [show-names](/ref/%7Bskin%7D/param/show-names.md) -m
*   [small-icons](/ref/%7Bskin%7D/param/small-icons.md) -m
*   [style](/ref/%7Bskin%7D/param/style.md) -m
*   [visited-color](/ref/%7Bskin%7D/param/visited-color.md) -m


Sending output to a grid looks like this:
### Example:

```
 // output to column 3, row 2 winset(usr, \"thegrid\",
\"current-cell=3,2\") usr \<\< output(\"Text\", \"thegrid\") // or even
easier* usr \<\< output(\"Text\", \"thegrid:3,2\") // when is-list is
true* usr \<\< output(\"5th item\", \"thegrid:5\") 
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
    proc](/ref/proc/output.md) -m which can be clicked, dragged, etc.; it will
    not act as a link.
-   The same margin is used all around the cell, not different margins
    for left, right, top, bottom.
-   There will always be a 1-pixel space for grid lines, whether
    they\'re shown or not.