# connection var (client) 
###### BYOND Version 487


This is a read-only var describing the type of client that is
connected.
**Possible values:**
+   \"seeker\" - The player is connected through Dream Seeker
+   \"telnet\" - The player is connected through telnet
+   \"world\" - The client is actually a world.Export() connection from
    another server
+   \"cgi\" - The client is connected via CGI (irrelevant to most
    worlds)
+   \"web\" - The client is connected via the Web client
+   \"http\" - The client is an HTTP connection (used by the Web
    client\'s virtual server)


Other values may be supported in the future. 

An empty
value means the connection type is unknown because a full handshake
hasn\'t been completed yet.

> [!TIP] 
> 