
## New (proc)

**Format:**
+   New(loc)
+   

**Arguments:**
+   loc: The initial location.

**Called When:**
+   Called when the object is created.

**Default Action:**
+   None.
***
By the time New() is called, the object has already been created at the specified location and all of its variables have been initialized. You can perform additional initialization by overriding this procedure.

Since the initial location parameter passed to <code>new()</code> is applied before New() is even called, there is some special handling of the `loc` variable when using named arguments in a call. Normally, if a procedure is overridden, named arguments in a call are matched against those in the the overridden definition. In this case, however, the `loc` parameter name is hard-coded. Regardless of what you call the first argument in your definition of New(), the initial location will be taken from the first positional argument, or from the argument named `loc` if there are no positional arguments.

The following example does some extra initialization that is not possible in the variable definition section, because it requires a runtime evaluation. This is a common reason to use New().


```dm

mob
   var
      birthdate //time stamp
   New()
      birthdate = world.realtime
      return ..()
   verb/look()
      set src in view()
      usr << "[src] was born on [time2text(birthdate,"DD-MMM-YYYY")]."

```

***
**Related Pages:**
+    [New proc (datum)](/ref/datum/proc/New)
+    [new proc](/ref/proc/new)
