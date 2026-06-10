
## game_state (var)
***
At runtime, this value may be changed to let the BYOND hub know about certain changes in the game's status. An example for using this value is if the number of players in the game gets too high and most new logins are rejected, you can set game_state to 1 to let the hub know this server is full.

The following values are accepted:

Note that this value does not affect how your world actually reacts to new players logging in. It is only used by the hub and website.
***