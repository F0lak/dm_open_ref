## executor var (world)
**See also:**
+   [startup proc](/ref/proc/startup.md) <!-- -->
**Format:**
+   executor = \"/usr/local/byond/bin/DreamDaemon \[params\]\"


This option is for direct execution of `.dmb` files in UNIX.
The most common use is for writing CGI programs that are executed by the
web server. 

The first parameter in the `executor`{.variable}
text string is the path to DreamDaemon. The one listed above is the
standard UNIX location. 

Optional parameters may follow. The
most common are -CGI and -logself.
### Example:

```
 world/executor = \"/usr/local/byond/bin/DreamDaemon -CGI
-logself\" 
```
 

This example creates a CGI program to be
executed by a web server. It puts its error output in the file
`projname`{.variable}`.log`. 

All of this is configured for you
when you include `html/CGI.dm` from the html library.