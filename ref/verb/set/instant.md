[]{#/instant setting (verb).md}    
## instant setting (verb)    
**See also:**    
:   [settings (verb)]/verb/set    
<!-- -->    
**Format:**    
:   set instant = Setting    
<!-- -->    
**Args:**    
:   Setting: 1 for \"instant\" verbs; 0 otherwise.    
<!-- -->    
**Default value:**    
:   0    
Normally a player can only call one verb per tick, but they can call any    
number of \"instant\" verbs in the same tick. This setting is useful for    
commands called by the game\'s interface, or for more responsive    
controls like for instance the use of \"combos\" in fighting games.    
Verbs with the instant setting can be used on the same tick as a regular    
verb, but only one regular verb can be used each tick. Instant commands    
will jump ahead of non-instant commands in the queue.    
Any verbs that are already built-in, such as movement commands, cannot    
be modified to use this setting. (Some, such as mouse commands, already    
use it.) You can, however, create replacement verbs of your own for most    
of them.    
### Example:    
mob/verb/FastNorth() set instant = 1 usr.Move(get_step(usr,NORTH),    
NORTH)  