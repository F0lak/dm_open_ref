[]{#/verbs.md}    
## verbs.mds    
**See also:**    
:   [arguments (verbs.md)]/verbs.md/arguments    
:   [settings (verbs.md)]/verbs.md/set    
:   [vars (verbs.mds)]/verbs.md/var    
:   [src var (proc)]/proc/var/src    
:   [usr var (proc)]/proc/var/usr    
Verbs may be attached to mobs, objs, turfs, and areas. Players can then    
use them as commands if they have access to the source.    
Verbs are fundamentally the same \"type\" as procs, so their vars are    
the same.    
### Example:    
mob/verbs.md/poof() world \<\< \"POOF!\"    
Whenever a player in the world types the command \"poof\", this verbs.md    
will be invoked.    
In addition to the normal access control (see the verbs.md src setting)    
verbs.mds can be dynamically added and removed from objects. One way to do    
this is to use new() with the following syntax: new    
verbs.md_path(Destination,Name,Desc)    
The Destination specifies the object to receive the verbs.md. Name and Desc    
optionally specify a new name and description for the verbs.md.    
### Example:    
mob/DM/verbs.md/kill(mob/M) del(M) mob/DM/verbs.md/give_kill_verbs.md(mob/M)    
new/mob/DM/verbs.md/kill(M)    
This example defines two verbs.mds (accessible to mobs of type /mob/DM). One    
verbs.md kills other mobs. The other adds the kill verbs.md to another mob    
(giving the second mob the ability to kill).    
In some situations, the ability to dynamically change an object\'s verbs.md    
list is quite useful, but most of the time it is far more convenient to    
do the same thing by manipulating objects rather than verbs.mds directly.    
For example, the previous example can be handled by having an object    
with the kill verbs.md attached it it. Then players have greater versatility    
in manipulating the verbs.md by simply moving the object around.    
### Example:    
obj/scroll/kill/verbs.md/kill(mob/M) set src = usr.contents //implicit src    
del(M)    
The use of an implicit verbs.md source in this example gives the user access    
to the kill verbs.md without having to specify the source scroll as long as    
the scroll exists in the user\'s inventory. In other words, the player    
types \"kill rat\" rather than \"kill kill rat\".  