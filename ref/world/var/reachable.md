## reachable var (world) 
###### BYOND Version 502
**See also:**
+   [port var (world)](/ref/world/var/port.md) 
+   [OpenPort proc (world)](/ref/world/proc/OpenPort.md) 

Returns 1 if the world is currently hosted and the port can be
reached by players (as determined by the BYOND hub), 0 if not.


If the port is not reachable, there may be a brief period
during which the hub is still attempting to make contact; during that
time the port is assumed to be reachable. Currently, the reachability
test times out and fails after 30 seconds.