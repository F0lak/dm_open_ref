## OpenPort proc (world)
**See also:**
*   [port var (world)](/world/var/port)
*   [visibility var (world)](/world/var/visibility)
<!-- -->
**See also:**
*   OpenPort(port=0)
<!-- -->
**Args:**
*   port* the network port to open
<!-- -->
**Returns:**
*   1 on success; 0 on failure


This causes the world to be hosted on the specified network
port. A value of 0 or \"any\" requests that any available port be used.
The value \"none\" causes the port to be closed so that no new
connections are possible. 

This proc may be overridden. If it
is, calling ..() is necessary to open the port. If ..() is not called,
it will not open.
### Example:

```
 world/OpenPort(port) // only allow subscribers to host
if(host_is_subscribed) return ..() 
```
 

The \"ports\"
configuration option in cfg/byond.txt can be used to control what ports
worlds may open. The -ports command-line option may also be used. See
[startup](/proc/startup) for the syntax.