## internet_address var (world)    
**See also:**    
:   [port var (world)](/world/var/port)    
:   [url var (world)](/world/var/url)    
:   [address var (world)](/world/var/address)    
This is the network address of the machine hosting the world, as it is    
seen by the outside network (from the Internet) and the hub. If it    
cannot be determined, it will be null.    
The full network address of the world may be formed by concatenating the    
world address and port: \"byond://\[address\]:\[port\]\".    
This var exists because `world.address` may not be accurate if the world    
is hosted on a machine behind a router using NAT. The value returned by    
`internet_address` can be given to other players who wish to log in.  