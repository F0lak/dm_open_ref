
## movement_mode (var)
***
Controls how movement works on the map.

`TILE_MOVEMENT_MODE` allows you to easily discard any and all pixel movement, so if step_x or step_y coordinates or unexpected atom bounds were loaded from a savefile, for instance, they would be eliminated. If you use any other movement mode, you can give an atom the <a class="code" href="#/atom/var/appearance_flags">TILE_MOVER</a> flag and it will behave as if it were in this mode, while other atoms are free to do their own thing.

`LEGACY_MOVEMENT_MODE` exists to distinguish between old and new movement behavior. In older versions of BYOND before pixel movement, turfs took their contents into consideration by default in Enter() and Exit(). This doesn't really make sense for newer games, so in any other movement mode the turf behavior will ignore its contents. mob.Cross() is also affected, since it would return 0 by default in legacy mode when both mobs were dense; now by default it checks `mob.group`.
***