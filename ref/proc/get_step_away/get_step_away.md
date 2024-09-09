[]{#/proc/get_step_away}    
## get_step_away proc    
**See also:**    
:   [step_away proc](/ref/proc/step_away/step_away.md)    
:   [walk_away proc](/ref/proc/walk_away/walk_away.md)    
<!-- -->    
**Format:**    
:   get_step_away(Ref, Trg, Max=5)    
<!-- -->    
**Returns:**    
:   The location of the new position, or 0 if no change.    
<!-- -->    
**Args:**    
:   Ref: Starting point or object.    
:   Trg: An object on the map.    
:   Max: The maximum distance between Ref and Targ before movement    
    halts.    
Calculate position of a step from `Ref` on a path away from `Trg`,    
taking obstacles into account. If `Ref` is farther than `Max` steps from    
`Trg`, 0 will be returned.  