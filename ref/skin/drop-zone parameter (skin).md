[]{#/{skin}/param/drop-zone}    
## drop-zone parameter (skin)    
**See also:**    
:   [mouse handling](/ref/DM/mouse.md)    
<!-- -->    
**Applies to:**    
:   [All](/ref/%7Bskin%7D/control.md)    
<!-- -->    
**Format:**    
:   true/false    
<!-- -->    
**Default value:**    
:   `true` for [Grid](/ref/%7Bskin%7D/control/grid.md),    
    [Info](/ref/%7Bskin%7D/control/info.md), [Map](/ref/%7Bskin%7D/control/map.md)    
:   `false` for everything else    
True if dragged objects may be dropped here. Default is true for Map,    
Info, and Grid controls, false for others. When in use, this will be the    
value of the `over_control` argument in    
[MouseDrop()](/ref/client/proc/MouseDrop.md){.code} if you drop an atom here.    
Grids can also add `drag-cell` and `drop-cell` to mouse proc parameters.    
The mouse procs\' `src_location` and `over_location` arguments are in    
the form `"[column],[row]"` (or `"[item"]` if    
[is-list](/ref/%7Bskin%7D/param/is-list.md){.code} is true) when dragging    
to/from a grid cell.    
In Info controls, `src_location` and `over_location` in mouse procs will    
be the name of the statpanel tab.  