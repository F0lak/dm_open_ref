
## startup (proc)

**Format:**
+   startup(File,Port=0,Options,...)

**Arguments:**
+   File: The dmb file to run in a new server or null to load the current world.
+   Port: The network port to start the new server on.  A value of 0
          indicates that any available port should be used.
+   Options: Any number of the options listed below.  Each option should be
             in an argument by itself.  If the option takes a parameter, this
             can be in the same argument or in the following one.

**Returns:**
+   The address of the new server in the form ip:port.
******
**Related Pages:**
+    [params](/ref/world/var/params)
+    [shutdown proc](/ref/proc/shutdown)
