## URL (client script)
**Format:**
*   #define URL \"byond://byond.com:6000\"


Defining a URL in a script, specifies the world to connect to
when the script is executed by the player. This is referred to as a
connection script, because the player uses it to connect to a world.
Other post-connection scripts such as `byond.dms` or a script loaded
through `client.script` are only used to configure the client after it
has connected to a world. In those cases, the URL setting has no effect.


It is important to enclose the URL in double quotes. Otherwise,
the `//` symbol would be mistaken for a comment.