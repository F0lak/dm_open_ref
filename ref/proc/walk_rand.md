[]{#/walk_rand proc.md}    
## walk_rand proc    
**See also:**    
:   [get_step_rand proc]/proc/get_step_rand    
:   [step_rand proc]/proc/step_rand    
:   [step_size var (movable atom)]/atom/movable/var/step_size    
<!-- -->    
**Format:**    
:   walk_rand(Ref,Lag=0,Speed=0)    
<!-- -->    
**Args:**    
:   Ref: A mob or obj.    
:   Lag: Delay in world ticks between movement.    
:   Speed: Speed to move, in pixels. 0 uses Ref.step_size.    
Moves Ref randomly. Each step will be preceded by Lag time of    
inactivity.    
A call to a walking function aborts any previous walking function called    
on Ref. To halt walking, call walk(Ref,0).    
This function returns immediately, but continues to process in the    
background.  