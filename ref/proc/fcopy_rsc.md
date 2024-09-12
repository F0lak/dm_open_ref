## fcopy_rsc proc
**See also:**
+   [cache](/ref/DM/cache.md) 
+   [fcopy proc](/ref/proc/fcopy.md) 
+   [file proc](/ref/proc/file.md) 
+   [load_resource proc](/ref/proc/load_resource.md) <!-- -->
**Format:**
+   fcopy_rsc(File)
<!-- -->
**Args:**
+   File+ file to copy into the resource cache
<!-- -->
**Returns:**
+   reference to the file as a cache entry


The file to copy may either be a file name (text string) or the
return value of file() operating on the same. If a cache entry is passed
as the argument, it will simply be returned with no action necessary.


Once a file has been copied into the resource cache (i.e. the
world\'s .rsc file), it may be used as an icon or a sound or whatever is
appropriate. Most internal operations involving resource files
automatically perform this operation when you try to use an external
file in place of a cache entry. For example, when assigning a file()
object to atom.icon, fcopy_rsc() is implicitly invoked. 

The
main reason you would ever want to call this explicitly is if you are
storing references to resource files in your own data structures and you
want to ensure that all values are converted to cache entries so they
may be directly compared to one another.