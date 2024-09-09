[]{#/atom/proc/Cross}    
## Cross proc (atom) {#cross-proc-atom byondver="490"}    
**See also:**    
:   [Enter proc (atom)](ref/atom/proc/Enter)    
:   [Entered proc (atom)](ref/atom/proc/Entered)    
:   [Exit proc (atom)](ref/atom/proc/Exit)    
:   [Exited proc (atom)](ref/atom/proc/Exited)    
:   [Crossed proc (atom)](ref/atom/proc/Crossed)    
:   [Uncross proc (atom)](ref/atom/proc/Uncross)    
:   [Uncrossed proc (atom)](ref/atom/proc/Uncrossed)    
:   [Move proc (movable atom)](ref/atom/movable/proc/Move)    
:   [group var (mob)](ref/mob/var/group)    
:   [movement_mode var (world)](ref/world/var/movement_mode)    
:   [Pixel movement](ref/%7Bnotes%7D/pixel-movement)    
<!-- -->    
**Format:**    
:   Cross(atom/movable/O)    
<!-- -->    
**Returns:**    
:   1 to permit; 0 to deny.    
<!-- -->    
**When:**    
:   Called when another object attempts to overlap this one.    
<!-- -->    
**Args:**    
:   O: the object attempting to overlap.    
<!-- -->    
**Default action:**    
:   Allow overlap unless both atoms are dense. If both atoms are mobs,    
    the behavior depends partly on whether they are in the same group.    
The following behavior only applies to    
[LEGACY_MOVEMENT_MODE](ref/world/var/movement_mode){.code}. In other    
movement modes, src.Cross(O) returns 0 by default if src and O are both    
mobs in the same group.    
If src completely covers the turf it is standing on, Cross() is called    
as part of turf.Enter(). This is to preserve the behavior of older    
games, which expect turf.Enter() to care about its contents.    
If src and O are both mobs, and O is in src\'s group, overlap is allowed    
*unless* neither of them use pixel movement. Older games that do not use    
pixel movement expect that Bump() will be called, and by default Bump()    
will swap the mobs\' positions. Swapping obviously only works in    
situations where a mob takes up a whole tile and only moves by tiles;    
for all other situations, allowing an overlap makes more sense.  