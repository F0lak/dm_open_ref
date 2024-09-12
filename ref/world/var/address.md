## address var (world)
**See also:**
*   [port var (world)](/ref/world/var/port.md) 
*   [url var (world)](/ref/world/var/url.md) 
*   [internet_address var (world)](/ref/world/var/internet_address.md) 

This is the network address of the machine hosting the world.
If it cannot be determined, it will be null. 

The full network
address of the world may be formed by concatenating the world address
and port* \"byond://\[address\]:\[port\]\". 

In CGI mode, this
is the web address of the world. 

This is the local address
only. If the world is hosted via a router, the external IP address may
be different. Use `internet_address` to find the external address, if
available.