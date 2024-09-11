## virtual_eye var (client)
**See also:**
*   [edge_limit var (client)](/ref/client/var/edge_limit.md) -m
*   [eye var (client)](/ref/client/var/eye.md) -m
*   [lazy_eye var (client)](/ref/client/var/lazy_eye.md) -m
*   [mob var (client)](/ref/client/var/mob.md) -m
*   [perspective var (client)](/ref/client/var/perspective.md) -m
*   [view var (client)](/ref/client/var/view.md) -m<!-- -->
**Default value:**
*   client.eye


This value determines the actual center of the player\'s map
display. It is based on `client.eye` and whenever possible matches it;
however it may instead be a turf, or null, when the eye is off-center.


The value of `virtual_eye` is read-only.