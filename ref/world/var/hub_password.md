## hub_password var (world)
**See also:**
+   [hub var (world)](/ref/world/var/hub.md) 
+   [visibility var (world)](/ref/world/var/visibility.md) <!-- -->
**Default value:**
+   null


If `world.hub` is set, any live session of the game will be
attached to the specified BYOND Hub page. Under the default settings,
any game can set `world.hub` and attach itself to any BYOND Hub page.


To beef up security, you can set a hub password in your hub\'s
configuration page via the BYOND website. This will ensure that only
authorized copies of your game can attach themselves to your hub page
when live. Then simply copy that password into your code as
`world.hub_password` so that your game\'s live broadcast will be
accepted by the hub.
### Example:

```
 world hub = \"Dan.PipeStock\" //registered hub path
hub_password = \"UPAggnJaeXmSBoKK\" //password for live game
authentication 
```
 

Note that for security reasons,
reading this variable at runtime will return a hashed version of the
value that was set.