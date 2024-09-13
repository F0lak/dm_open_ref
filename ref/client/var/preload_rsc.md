# preload_rsc var (client)
**Default value:**
+   1\.


This variable controls whether resource files (icons and
sounds) are automatically downloaded by Dream Seeker when first
connecting, or whether they should be downloaded as needed. Resource
files are cached (in byond.rsc) for future use, so this should only
affect people who have not played the game before or who have not played
it for some time. 

The three possible settings are:
0
+   do not preload any resources
1
+   preload compiled-in resources only
2
+   preload all resources including those uploaded by players
URL
+   preload resources from specified file


Preloading resource files will eliminate delays later on, but
may cause a very long initial delay when logging in. 

Resources
may also be distributed from a website to save bandwidth on the machine
hosting the game. Simply zip up the .rsc file, upload it to a web site,
and put the URL here.
### Example:

``` dm
 client/preload_rsc =
\"http://dan.byond.com/mygame_rsc.zip\" 
```
 

Instead of
putting the .rsc file in the .zip, you can also put the individual
resource files there. This would allow you to select specific files that
you would like to be preloaded. For example, you could create a
different resource package for different parts of the game world and
assign client.preload_rsc dynamically as the player moves into each
different area. 

Once Dream Seeker has downloaded a resource
package, it caches it and will not download it again, even if you upload
a new version of the file. This allows you to make small changes without
forcing a complete refresh. Any files which are not found in the preload
package are simply downloaded from the game server directly. 

If
you want to force a complete refresh, simply change the name of the
resource package. For example, you could put a version number in the
name of the file: `mygame_rsc_01.zip`, `mygame_rsc_02.zip`, and so on.