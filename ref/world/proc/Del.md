## Del proc (world)

**Format:**
+   Del()
<!-- -->
**When:**
+   Called when the world is shutdown.
<!-- -->
**Default action:**
+   Shutdown the world.


When the world is destroyed, only the Del() proc of the `world`
object is called automatically. If you want to delete any other objects,
you must do so from within `world/Del()`. Once this procedure returns,
any other procedures which may still be executing are immediately
aborted and all objects are silently destroyed. 

To prevent
accidental hangs during `world/Del()` from preventing shutdown, a
timeout is applied to any sleeping operations such as `sleep`,
`world.Export()`, and so on. If the total time slept exceeds the
timeout, `world/Del()` is aborted. Currently, this timeout is set at 30
seconds.

**See also:**
+   [Del proc (datum)](/ref/datum/proc/Del.md) 
+   [shutdown proc](/ref/proc/shutdown.md) <!-- -->