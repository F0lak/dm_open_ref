[]{#/eye var (client).md}    
## eye var (client)    
**See also:**    
:   [edge_limit var (client)]/client/var/edge_limit    
:   [lazy_eye var (client)]/client/var/lazy_eye    
:   [mob var (client)]/client/var/mob    
:   [perspective var (client)]/client/var/perspective    
:   [glide_size var (client)]/client/var/glide_size    
:   [view var (client)]/client/var/view    
:   [virtual_eye var (client)]/client/var/virtual_eye    
:   [view var (world)]/world/var/view    
:   [step_x var (movable atom)]/atom/movable/var/step_x    
:   [step_y var (movable atom)]/atom/movable/var/step_y    
<!-- -->    
**Default value:**    
:   The connected mob, client.mob.    
This value determines the center of the player\'s map. The default value    
simply means that the visible region is normally centered on the    
player\'s mob. Effects such as setting `perspective` to    
`EDGE_PERSPECTIVE` or using `lazy_eye` can move the map off-center    
temporarily. The eye is the *ideal* center, not necessarily the actual    
center; to find the actual center, use `virtual_eye`.    
The eye\'s step_x/y vars, if present, are also used to allow smooth    
scrolling of the map. These also obey lazy_eye and edge_limit.    
Note that the visibility of objects is still computed from the point of    
view of the mob rather than the eye. This allows the use of `lazy_eye`    
or similar effects that control the panning of the map while still    
having the player see only what the mob can see. To determine visibility    
from the eye, you can change the value of `client.perspective`.    
If a player connects to a new mob M, client.eye automatically changes to    
M.    
### Example:    
client eye = locate(5,5,1)    
This fixes the center of the player\'s map at the turf coordinate    
(5,5,1). Since the eye is fixed, the map will not scroll even as the    
player\'s mob moves out of the visible range.  