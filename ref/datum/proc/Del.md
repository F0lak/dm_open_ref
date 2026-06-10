
## Del (proc)

**Format:**
+   Del()

**Called When:**
+   Called when the object is destroyed, for example by using the
 instruction.

**Default Action:**
+   Delete the object.  The contents of atomic objects are also destroyed at
this time, as though  were called on each one of them.
***
When the world is destroyed, the `Del()` proc is not automatically called. The only object for which it is called is <a href="#/world">/world</a>. If you need the `Del()` proc for a particular object to be called at that time, you should explicitly call it from `world/Del()`.

Note: **Always** call `..()` at the end of the proc if you override it.
***
**Related Pages:**
+    [del proc](/ref/proc/del)
+    [garbage collection](/ref/DM/garbage)
