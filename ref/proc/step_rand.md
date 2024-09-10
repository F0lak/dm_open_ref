[]{#/step_rand proc.md}    
## step_rand proc    
**See also:**    
:   [get_step_rand proc](/proc/get_step_rand)    
:   [walk_rand proc](/proc/walk_rand)    
:   [step_size var (movable atom)](/atom/movable/var/step_size)    
<!-- -->    
**Format:**    
:   step_rand(Ref,Speed=0)    
<!-- -->    
**Returns:**    
:   1 on success; 0 otherwise.    
<!-- -->    
**Args:**    
:   Ref: A mob or obj.    
:   Speed: Speed to move, in pixels. 0 uses Ref.step_size.    
Move Ref randomly.  