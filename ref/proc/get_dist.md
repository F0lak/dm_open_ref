[]{#/get_dist proc.md}    
## get_dist proc    
**See also:**    
:   [bounds_dist proc]/proc/bounds_dist    
<!-- -->    
**Format:**    
:   get_dist(Loc1, Loc2)    
<!-- -->    
**Returns:**    
:   The distance between `Loc1` and `Loc2`, in tiles. This is the number    
    of full-tile movements (disregarding any obstacles and allowing    
    diagonal moves *including across Z levels*) required to go from one    
    to the other. You can think of it as the max of their x, y, and z    
    distances.    
<!-- -->    
**Args:**    
:   Loc1: An object on the map.    
:   Loc2: An object on the map.    
For a distance in pixels, use `bounds_dist()`.    
`get_dist()` will return -1 when `Loc1` and `Loc2` are the same object.    
If one or both of them is not on the map, an infinite value is returned.    
Note: Prior to BYOND 515, `get_dist()` never returned a value greater    
than 127, which it counted as \"infinite\".  