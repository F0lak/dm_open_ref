
## FILE_DIR (info)

**Format:**
+   #define FILE_DIR Path

**Arguments:**
+   Path: A search path on the current filesystem.
***
This macro defines a search path to be used in evaluating resource files (icons and sounds). First the current directory is searched, then the first <code>FILE_DIR</code> path, then the next, etc.


```dm

#define FILE_DIR icons
#define FILE_DIR icons/mobs

mob/clown
  icon = 'clown.dmi'

```


This searches for the file at the paths <code>"./clown.dmi"</code>, <code>"./icons/clown.dmi"</code>, and <code>"./icons/sounds/clown.dmi"</code>, where <code>"."</code> is the directory of the current source file.
***
**Related Pages:**
+    [cache](/ref/DM/cache)
+    [icons](/ref/DM/icon)
