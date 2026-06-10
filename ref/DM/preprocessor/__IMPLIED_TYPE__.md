
## __IMPLIED_TYPE__ (info)
***
The `__IMPLIED_TYPE__` macro is replaced by a reference to the type path implied at the current point in compilation. For instance, when using the <a href="#/proc/new">`new` proc</a> and assigning to a var, the type path for `new()` is implied by the var's type. Implied types are also automatically used in <a class="code" href="#/proc/locate">locate()</a>, and are used by default for the second argument in <a class="code" href="#/proc/istype">istype()</a> and <a class="code" href="#/proc/astype">astype()</a>.


```dm

proc/Factory(new_type)
    world.log << "Creating new [new_type]"
    return new new_type()

proc/CreateThing()
    // pass /thing to Factory
    var/thing/T = Factory(__IMPLIED_TYPE__)

```


`__IMPLIED_TYPE__` is valid in the following situations:

This is actually a pseudo-macro; the preprocessor doesn't handle it directly.
***
**Related Pages:**
+    [__FILE__ macro](/ref/DM/preprocessor/__FILE__)
+    [__LINE__ macro](/ref/DM/preprocessor/__LINE__)
+    [__PROC__ macro](/ref/DM/preprocessor/__PROC__)
+    [__TYPE__ macro](/ref/DM/preprocessor/__TYPE__)
+    [new proc](/ref/proc/new)
+    [locate proc](/ref/proc/locate)
+    [istype proc](/ref/proc/istype)
+    [astype proc](/ref/proc/astype)
