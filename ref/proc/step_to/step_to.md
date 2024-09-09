[]{#/proc/step_to}    
## step_to proc    
**See also:**    
:   [get_step_to proc](/ref/proc/get_step_to)    
:   [get_steps_to proc](/ref/proc/get_steps_to)    
:   [walk_to proc](/ref/proc/walk_to)    
:   [step_size var (movable atom)](/ref/atom/movable/var/step_size)    
<!-- -->    
**Format:**    
:   step_to(Ref,Trg,Min=0,Speed=0)    
<!-- -->    
**Returns:**    
:   1 on success; 0 otherwise.    
<!-- -->    
**Args:**    
:   Ref: A mob or obj.    
:   Trg: An object on the map.    
:   Min: The minimum distance between Ref and Trg before movement halts.    
:   Speed: Speed to move, in pixels. 0 uses Ref.step_size.    
Move Ref on a path to the location Trg, taking obstacles into account.    
If Ref is within Min steps of Trg, no action will be taken. This is also    
the case if the target is too far away (more than twice world.view    
steps).  