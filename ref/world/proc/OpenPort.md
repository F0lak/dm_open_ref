
## OpenPort (proc)
***
This causes the world to be hosted on the specified network port. A value of 0 or "any" requests that any available port be used. The value "none" causes the port to be closed so that no new connections are possible.

This proc may be overridden. If it is, calling ..() is necessary to open the port. If ..() is not called, it will not open.


```dm

world/OpenPort(port)
  // only allow subscribers to host
  if(host_is_subscribed)
    return ..()

```


The "ports" configuration option in cfg/byond.txt can be used to control what ports worlds may open. The -ports command-line option may also be used. See <a href="#/proc/startup">startup</a> for the syntax.
***