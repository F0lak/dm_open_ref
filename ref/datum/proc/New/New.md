[]{#/datum/proc/New}    
## New proc (datum)    
**See also:**    
:   [New proc (atom)](/ref/atom/proc/New.md)    
:   [New proc (client)](/ref/client/proc/New.md)    
:   [new proc](/ref/proc/new.md)    
<!-- -->    
**Format:**    
:   New()    
<!-- -->    
**When:**    
:   Called when the datum is created, for example by using `new`, when    
    reading an object that was stored in a [savefile](/ref/savefile.md), or    
    when the world is initially created.    
<!-- -->    
**Default action:**    
:   None.    
You can use the New() procedure to do more complicated initializations    
than are possible in the object definition where you assign the initial    
value of variables to constants.    
The following example makes use of the \"Location\" parameter that is    
passed to objects of type [/atom](/ref/atom.md). You can pass any number of    
additional arguments to New() by passing them to the `new` instruction    
which creates the object.    
### Example:    
mob/night var/mob/squire/my_squire New(Location) my_squire =    
new(Location) return ..()    
Also note that the type of object being created in this case was    
automatically inferred from the variable type on the left-hand side of    
the assignment. That\'s a handy little DM short-cut.  