
## cache (info)
***
Files specified in single quotes are loaded (at compile time) into the world cache file (ending in <code>.rsc</code>). These are referred to as resource files. At runtime these files are downloaded by players into their <code>byond.rsc</code> file for future use. With the appropriate verbs or through savefiles, players may also upload files into the world cache.

If a resource file is not used for a long time, it will be automatically removed from the cache file to save space. If a cache file gets too bulky, however, you may manually delete it and start from scratch.

To make compilation faster and to make it easier to distribute code, the compiler will use an existing cache file if possible. That means you could compile up a world, and send people the <code>.dm</code> and <code>.rsc</code> files without any need to package all the individual resource files. It is also possible to include additional supplementary <code>.rsc</code> files by using the <code>#include</code> statement.
***
**Related Pages:**
+    [FILE_DIR definition](/ref/DM/preprocessor/define/FILE_DIR)
+    [cache_lifespan](/ref/world/var/cache_lifespan)
+    [fcopy_rsc proc](/ref/proc/fcopy_rsc)
+    [file proc](/ref/proc/file)
+    [icons](/ref/DM/icon)
+    [sounds](/ref/DM/sound)
