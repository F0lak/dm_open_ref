## verbs
**See also:**
*   [arguments (verb)](/ref/verb/arguments.md) -m
*   [settings (verb)](/ref/verb/set.md) -m
*   [vars (verbs)](/ref/verb/var.md) -m
*   [src var (proc)](/ref/proc/var/src.md) -m
*   [usr var (proc)](/ref/proc/var/usr.md) -m

Verbs may be attached to mobs, objs, turfs, and areas. Players
can then use them as commands if they have access to the source.


Verbs are fundamentally the same \"type\" as procs, so their
vars are the same.
### Example:

```
 mob/verb/poof() world \<\< \"POOF!\" 
```



Whenever a player in the world types the command \"poof\", this
verb will be invoked. 

In addition to the normal access control
(see the verb src setting) verbs can be dynamically added and removed
from objects. One way to do this is to use new() with the following
syntax* 
```
 new verb_path(Destination,Name,Desc) 
```



The Destination specifies the object to receive the verb. Name
and Desc optionally specify a new name and description for the verb.
### Example:

```
 mob/DM/verb/kill(mob/M) del(M)
mob/DM/verb/give_kill_verb(mob/M) new/mob/DM/verb/kill(M) 
```



This example defines two verbs (accessible to mobs of type
/mob/DM). One verb kills other mobs. The other adds the kill verb to
another mob (giving the second mob the ability to kill). 

In
some situations, the ability to dynamically change an object\'s verb
list is quite useful, but most of the time it is far more convenient to
do the same thing by manipulating objects rather than verbs directly.
For example, the previous example can be handled by having an object
with the kill verb attached it it. Then players have greater versatility
in manipulating the verb by simply moving the object around.
### Example:

```
 obj/scroll/kill/verb/kill(mob/M) set src = usr.contents
//implicit src del(M) 
```
 

The use of an implicit verb
source in this example gives the user access to the kill verb without
having to specify the source scroll as long as the scroll exists in the
user\'s inventory. In other words, the player types \"kill rat\" rather
than \"kill kill rat\".