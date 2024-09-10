## dir var (client)    
**Default value:**    
:   NORTH    
This defines the relationship between the world\'s coordinate system and    
the player\'s screen. The default means that the player sees the map    
exactly as it was created (in the map-editor or at runtime). Changing it    
to one of the other directions causes the player to see the map as if it    
were rotated to that direction. This means that a player with client.dir    
= SOUTH would see the map inverted relative to a person with client.dir    
= NORTH. That\'s handy in two-player board games where you want both    
players to see their side in the same place.    
Note that this does not turn icons upside down! The map is rotated, but    
the icons on the map remain in their normal orientation.    
Movement keys are remapped so that a player with client.dir = SOUTH    
hitting the up arrow will generate a call to client.South() rather than    
the usual client.North().  