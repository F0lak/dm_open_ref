## rooms


Areas that are not located on the map are referred to as
*rooms*. When a player enters one, the map goes away and you have
something like a text MUD. By default, there would be no way for players
to move from one room to another, so you have to handle movement
yourself. 

You can check the variable [area.x](/atom/var/x) to
see if a given area is on the map or not. 

The following example
puts players in a room when they log in and provides a single exit.
### Example:

```
 mob/Login() if(!loc) Move(locate(/area/birthing_hut)) return
..() area/birthing_hut Entered(O) O \<\< \"Waaaaah! You land in a pile
of straw.\" return ..() verb/exit() if(Move(locate(1,1,1))) //jump to
the map or whatever usr \<\< \"You crawl into the open air\...\" else
usr \<\< \"The hut door is blocked. You cannot get out.\" 
```
