
## SoundQuery (proc)

**Format:**
+   SoundQuery()

**Arguments:**
+   none

**Returns:**
+   A list of  datums with information about currently playing sounds.
***
This proc is used to ask a client about sounds that are playing. The `/sound` datums in the returned list have the following vars set:

Not all info about the sounds is retrieved, such as `volume`, `frequency`, etc. If those are needed, it should be a simple matter to keep track of them in your code. The main purpose of `SoundQuery()` is to ascertain the current status of playing sounds.
***
**Related Pages:**
+    [sound datum](/ref/sound)
+    [sound proc](/ref/proc/sound)
