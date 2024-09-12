## version var (world)
**See also:**
*   [hub var (world)](/ref/world/var/hub.md) 
<!-- -->
**Default value:**
*   0


If you are distributing your game to players, you can use this
variable to automatically notify them of new releases. To do so, you
will first need to set [`world.hub`](/ref/world/var/hub.md) to the hub path of
your game. You can then advertise the current version by configuring
that value in your [hub
console](https://secure.byond.com/members/?command=edit_hub).


When players boot up an outdated version of your game (as
indicated by comparing `world.version` with the version advertised by
BYOND hub), they will be notified of the new release.