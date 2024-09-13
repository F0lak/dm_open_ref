## FILE_DIR definition

**Format:**
+   #define FILE_DIR Path
<!-- -->
**Args:**
+   Path: A search path on the current filesystem.


This macro defines a search path to be used in evaluating
resource files (icons and sounds). First the current directory is
searched, then the first `FILE_DIR` path, then the next, etc.
### Example:

``` dm
 #define FILE_DIR icons #define FILE_DIR icons/mobs
mob/clown icon = \'clown.dmi\' 
```
 

This searches for the
file at the paths `"./clown.dmi"`, `"./icons/clown.dmi"`, and
`"./icons/sounds/clown.dmi"`, where `"."` is the directory of the
current source file.

> [!TIP] 
> **See also:**
> +   [cache](/ref/DM/cache.md) 
> +   [icons](/ref/DM/icon.md) <!-- -->