[]{#/client/var/edge_limit}    
## edge_limit var (client)    
**See also:**    
:   [eye var (client)](/ref/client/var/eye/eye.md)    
:   [lazy_eye var (client)](/ref/client/var/lazy_eye/lazy_eye.md)    
:   [perspective var (client)](/ref/client/var/perspective/perspective.md)    
:   [view var (client)](/ref/client/var/view/view.md)    
:   [screen_loc var (movable atoms)](/ref/atom/movable/var/screen_loc/screen_loc.md)    
<!-- -->    
**Default value:**    
:   null    
This value determines the limits that a client\'s eye will display. If    
`client.perspective` uses the `EDGE_PERSPECTIVE` flag, the view    
shouldn\'t scroll beyond the bounds set by `edge_limit`. If the bounds    
of `edge_limit` are as big as or smaller than the client\'s view, no    
scrolling will occur even if `EDGE_PERSPECTIVE` is not used. Normally    
this value is null, which provides freedom for the eye to move anywhere    
on the map. It may be changed to a text value describing the limits in    
more detail.    
The format is similar to `atom.screen_loc` which uses    
`"[x1],[y1] to [x2],[y2]"`. It can also use directions such as    
`"SOUTHWEST to NORTHEAST"`, which refer to the limits of the map.    
### Example:    
area/house var/x1,x2,y1,y2 Entered(mob/M) if(ismob(M) && M.client)    
M.client.edge_limit = \"\[x1\],\[y1\] to \[x2\],\[y2\]\" Exited(mob/M)    
if(ismob(M) && M.client) M.client.edge_limit = null  