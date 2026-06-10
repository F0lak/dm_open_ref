
## istype (proc)

**Format:**
+   istype(Val,Type)
+   istype(Val)

**Arguments:**
+   Val:  An object instance.
+   Type: An object prototype or instance.  If no type is specified and a
     variable was passed in as the first argument, it will default to the
     declared type of the variable.

**Returns:**
+   1 if Val is derived from Type; 0 otherwise.
***
If you don't have an object instance to test, but just want to see if one prototype derives from another one, use <a href="#/proc/ispath">ispath()</a> instead.


```dm

var/M
M = new/mob/ugly/duckling()
if(istype(M,/mob/ugly))  //this will be true
  usr << "[M] is ugly!"

```


Using implicit types, that same example can be rewritten as follows:


```dm

var/mob/ugly/M
M = new/mob/ugly/duckling()
if(istype(M))  //this will be true
  usr << "[M] is ugly!"

```

***
**Related Pages:**
+    [ispath proc](/ref/proc/ispath)
+    [locate proc](/ref/proc/locate)
+    [typesof proc](/ref/proc/typesof)
+    [astype proc](/ref/proc/astype)
+    [__IMPLIED_TYPE__ macro](/ref/DM/preprocessor/__IMPLIED_TYPE__)
