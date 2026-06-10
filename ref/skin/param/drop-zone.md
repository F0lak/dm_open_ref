
## drop-zone (info)
***
True if dragged objects may be dropped here. Default is true for Map, Info, and Grid controls, false for others. When in use, this will be the value of the `over_control` argument in <a class="code" href="#/client/proc/MouseDrop">MouseDrop()</a> if you drop an atom here.

Grids can also add `drag-cell` and `drop-cell` to mouse proc parameters. The mouse procs' `src_location` and `over_location` arguments are in the form `"[column],[row]"` (or `"[item"]` if <a class="code" href="#/{skin}/param/is-list">is-list</a> is true) when dragging to/from a grid cell.

In Info controls, `src_location` and `over_location` in mouse procs will be the name of the statpanel tab.
***