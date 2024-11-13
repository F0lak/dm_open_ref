## Del proc (datum)

**Format:**
+   Del()

**When:**
+   Called when the object is destroyed, for example by using the `del`
    instruction, or during garbage collection.

**Default action:**
+   Delete the object. The contents of atomic objects are also destroyed
    at this time, as though `del` were called on each one of them.

When the world is destroyed, the `Del()` proc is not
automatically called. The only object for which it is called is
[/world](/ref/world.md)  If you need the `Del()` proc for a particular object
to be called at that time, you should explicitly call it from
`world/Del()`. 

> [!NOTE]
> **Always** call `..()` at the end of this
> proc if you override it. Not doing so will prevent the object from being destroyed.

> [!TIP] 
> **See also:**
> +   [del proc](/ref/proc/del.md) 
> +   [garbage collection](/ref/DM/garbage.md) 
