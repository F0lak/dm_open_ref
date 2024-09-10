## edge_limit var (client)    
**See also:**    
:   [eye var (client)](/client/var/eye)    
:   [lazy_eye var (client)](/client/var/lazy_eye)    
:   [perspective var (client)](/client/var/perspective)    
:   [view var (client)](/client/var/view)    
:   [screen_loc var (movable atoms)](/atom/movable/var/screen_loc)    
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