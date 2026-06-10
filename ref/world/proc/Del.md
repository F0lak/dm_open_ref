
## Del (proc)

**Format:**
+   Del()

**Called When:**
+   Called when the world is shutdown.

**Default Action:**
+   Shutdown the world.
***
When the world is destroyed, only the Del() proc of the <code>world</code> object is called automatically. If you want to delete any other objects, you must do so from within <code>world/Del()</code>. Once this procedure returns, any other procedures which may still be executing are immediately aborted and all objects are silently destroyed.

To prevent accidental hangs during <code>world/Del()</code> from preventing shutdown, a timeout is applied to any sleeping operations such as <code>sleep</code>, <code>world.Export()</code>, and so on. If the total time slept exceeds the timeout, <code>world/Del()</code> is aborted. Currently, this timeout is set at 30 seconds.
***
**Related Pages:**
+    [Del proc (datum)](/ref/datum/proc/Del)
+    [shutdown proc](/ref/proc/shutdown)
