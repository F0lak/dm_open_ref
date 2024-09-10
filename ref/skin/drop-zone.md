[]{#/drop-zone parameter (skin).md}/param/drop-zone}    
## drop-zone parameter (skin)    
**See also:**    
:   [mouse handling](/DM/mouse)    
<!-- -->    
**Applies to:**    
:   [All](/%7Bskin%7D/control)    
<!-- -->    
**Format:**    
:   true/false    
<!-- -->    
**Default value:**    
:   `true` for [Grid](/%7Bskin%7D/control/grid),    
    [Info](/%7Bskin%7D/control/info), [Map](/%7Bskin%7D/control/map)    
:   `false` for everything else    
True if dragged objects may be dropped here. Default is true for Map,    
Info, and Grid controls, false for others. When in use, this will be the    
value of the `over_control` argument in    
[MouseDrop()](/client/proc/MouseDrop){.code} if you drop an atom here.    
Grids can also add `drag-cell` and `drop-cell` to mouse proc parameters.    
The mouse procs\' `src_location` and `over_location` arguments are in    
the form `"[column],[row]"` (or `"[item"]` if    
[is-list](/%7Bskin%7D/param/is-list){.code} is true) when dragging    
to/from a grid cell.    
In Info controls, `src_location` and `over_location` in mouse procs will    
be the name of the statpanel tab.  