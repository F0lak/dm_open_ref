## Move proc (movable atom)    
**See also:**    
:   [Bump proc (movable atom)](/atom/movable/proc/Bump)    
:   [Enter proc (atom)](/atom/proc/Enter)    
:   [Entered proc (atom)](/atom/proc/Entered)    
:   [Exit proc (atom)](/atom/proc/Exit)    
:   [Exited proc (atom)](/atom/proc/Exited)    
:   [Cross proc (atom)](/atom/proc/Cross)    
:   [Crossed proc (atom)](/atom/proc/Crossed)    
:   [Uncross proc (atom)](/atom/proc/Uncross)    
:   [Uncrossed proc (atom)](/atom/proc/Uncrossed)    
:   [loc var (atom)](/atom/var/loc)    
:   [locs list var (movable atom)](/atom/movable/var/locs)    
:   [walk proc](/proc/walk)    
:   [Gliding](/%7Bnotes%7D/gliding)    
:   [Pixel movement](/%7Bnotes%7D/pixel-movement)    
<!-- -->    
**Format:**    
:   Move(NewLoc,Dir=0,step_x=0,step_y=0)    
<!-- -->    
**Returns:**    
:   Success (jump): 1    
:   Success (slide): Number of pixels moved    
:   Failure: 0    
<!-- -->    
**When:**    
:   Called to move the object. By default, client.Move() calls this proc    
    when players use direction keys. The automated movement functions    
    (like walk()) also call this proc. Directly setting the loc variable    
    does **not** call this procedure.    
<!-- -->    
**Args:**    
:   NewLoc: The new location.    
:   Dir: The direction of movement (or 0).    
:   [step_x]{byondver="490"}: The new step_x value, relative to NewLoc    
:   [step_y]{byondver="490"}: The new step_y value, relative to NewLoc    
Any Move() is either a slide or a jump. Normal walking around is a    
slide; it can be stopped partway. A jump is pass/fail. See more    
information below.    
This is what happens by default:    
1.  oldloc.Exit(src) is called for any turfs or areas being vacated, or    
    the container if moving out of an obj or mob. neighbor.Uncross(src)    
    is called for any atoms that will no longer be overlapping this    
    object. If any of these return 0 (failure), movement fails.    
2.  newloc.Enter(src) is called for any turfs or areas that may be    
    entered for the first time, or the container if moving into an obj    
    or mob. neighbor.Cross(src) is called for any atoms that may be in    
    collision with this object if the move fully succeeds. If any of    
    these return 0 (failure), then a slide can be cut short but a jump    
    will fail completely.    
3.  If any obstacles were encountered via Enter() or Cross() failing,    
    then src.Bump(obstacle) will be called for each of them.    
4.  If movement did not fail completely, then loc and step_x/y, will be    
    changed, and the following calls will be made: oldloc.Exited() for    
    any turfs, areas, or other containers vacated; neighbor.Uncrossed()    
    for any movable atoms no longer overlapping; newloc.Entered() for    
    any turfs, areas, or other containers being entered for the first    
    time; and neighbor.Crossed() for any movable atoms now overlapping    
    the object.    
A movement is considered a slide if src is moving from one turf to    
another on the same z level, and the total pixel distance is less than    
either src.step_size or a full tile size (whichever is largest). Any    
other movement is a jump. Movement to the same turf with no step_x/y    
change is also considered a jump.  