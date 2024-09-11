## Stat proc (client)
**See also:**
*   [Stat proc (atom)](/atom/proc/Stat)
*   [stat proc](/proc/stat)
*   [statobj var (client)](/client/var/statobj)
*   [statpanel proc](/proc/statpanel)
*   [statpanel var (client)](/client/var/statpanel)
*   [Info control (skin)](/%7Bskin%7D/control/info)
<!-- -->
**Format:**
*   Stat()
<!-- -->
**When:**
*   Called periodically by the client to update the stat window.
<!-- -->
**Default action:**
*   Call statobj.Stat().


If this procedure sleeps (or engages in some other waiting
operation), it will not be called again until it finally returns. This
allows you to effectively decrease the frequency of calls to the proc.
You might want to do that if it is a fairly lengthy procedure, and
frequent calls are slowing things down. 

To increase the
frequency of stat updates, you can lower `world.tick_lag`.


Note* Typically only the currently viewed statpanel is updated,
which saves on some network activity and a little time. If however the
proc sleeps, you need to be sure that any pending updates are displayed
once the right panel is available. Therefore if you\'re resetting a var
that indicates the proc should sleep next time, it should not be reset
unless you know the player is looking at the right statpanel and has
received the updates.
### Example

```
 client/var/updategold = 1 // set to 1 if gold changes
client/var/updateinventory = 1 // set to 1 if inventory changes
client/Stat() // if not ready to update, Stat() won\'t be called again
till sleep is done while(!updategold && !updateinventory) sleep(5)
if(statpanel(\"Gold\")) // switch to Gold panel and ask if player is
looking at it stat(\"Gold\", mob.gold) updategold = 0 // we updated, so
turn this flag back off if(statpanel(\"Inventory\")) stat(mob.contents)
updateinventory = 0 
```
 

Because sleeping in Stat()
requires more thinking through, it\'s best to do so only in cases where
Stat() has to do a lot of intensive calculations.