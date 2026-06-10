
## New (proc)

**Format:**
+   New()

**Called When:**
+   Called when the datum is created, for example by using ,
when reading an object that was stored in a ,
or when the world is initially created. [savefile](/ref/savefile)

**Default Action:**
+   None.
***
You can use the New() procedure to do more complicated initializations than are possible in the object definition where you assign the initial value of variables to constants.

The following example makes use of the "Location" parameter that is passed to objects of type <a href="#/atom">/atom</a>. You can pass any number of additional arguments to New() by passing them to the <code>new</code> instruction which creates the object.


```dm

mob/night
   var/mob/squire/my_squire
   New(Location)
      my_squire = new(Location)
      return ..()

```


Also note that the type of object being created in this case was automatically inferred from the variable type on the left-hand side of the assignment. That's a handy little DM short-cut.
***
**Related Pages:**
+    [New](/ref/atom/proc/New)
+    [New proc (client)](/ref/client/proc/New)
+    [new proc](/ref/proc/new)
