## get_step_to proc    
**See also:**    
:   [step_to proc](/proc/step_to)    
:   [walk_to proc](/proc/walk_to)    
:   [get_steps_to proc](/proc/get_steps_to)    
<!-- -->    
**Format:**    
:   get_step_to(Ref, Trg, Min=0)    
<!-- -->    
**Returns:**    
:   The location of the new position, or 0 if no change.    
<!-- -->    
**Args:**    
:   Ref: Starting point or object.    
:   Trg: An object on the map.    
:   Min: The minimum distance between Ref and Trg before movement halts.    
Calculate the position of a step from `Ref` on a path to `Trg`, taking    
obstacles into account.    
If `Ref` is within `Min` steps of `Trg`, no step is computed. This is    
also true if the target is too far away (more than twice `world.view`    
steps). In either case, null is returned.  