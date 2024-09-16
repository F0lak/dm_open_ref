# Command proc (client)
**Format:**
+   Command(command as command_text)
<!-- -->
**When:**
+   Called when the player types in something that is not understood as
    a valid command, or if the player is connected via telnet.
<!-- -->
**Default action:**
+   None.


If this proc is used, players will be able to connect to your
world via telnet. All telnet users\' commands are routed through this
proc instead of being parsed into verbs. Players who join the world
through Dream Seeker will have their commands parsed as verbs first, and
those commands will end up here only if there is no applicable verb.


Note that text received by this proc is not interpreted
beforehand, so quotes " and backslashes \\ should come through
unaltered. 

This proc is primarily useful if you want to handle
parsing yourself (like for a MUD), or if your world is a chat server and
verbs are not used much.