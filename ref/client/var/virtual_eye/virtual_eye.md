[]{#/client/var/virtual_eye}
## virtual_eye var (client)
**See also:**
:   [edge_limit var (client)](#/client/var/edge_limit)
:   [eye var (client)](#/client/var/eye)
:   [lazy_eye var (client)](#/client/var/lazy_eye)
:   [mob var (client)](#/client/var/mob)
:   [perspective var (client)](#/client/var/perspective)
:   [view var (client)](#/client/var/view)
<!-- -->
**Default value:**
:   client.eye
This value determines the actual center of the player\'s map display. It
is based on `client.eye` and whenever possible matches it; however it
may instead be a turf, or null, when the eye is off-center.
The value of `virtual_eye` is read-only.