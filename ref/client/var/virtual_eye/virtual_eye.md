[]{#/client/var/virtual_eye}    
## virtual_eye var (client)    
**See also:**    
:   [edge_limit var (client)](/ref/client/var/edge_limit/edge_limit.md)    
:   [eye var (client)](/ref/client/var/eye/eye.md)    
:   [lazy_eye var (client)](/ref/client/var/lazy_eye/lazy_eye.md)    
:   [mob var (client)](/ref/client/var/mob/mob.md)    
:   [perspective var (client)](/ref/client/var/perspective/perspective.md)    
:   [view var (client)](/ref/client/var/view/view.md)    
<!-- -->    
**Default value:**    
:   client.eye    
This value determines the actual center of the player\'s map display. It    
is based on `client.eye` and whenever possible matches it; however it    
may instead be a turf, or null, when the eye is off-center.    
The value of `virtual_eye` is read-only.  