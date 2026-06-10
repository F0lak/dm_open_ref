
## executor (var)
***
This option is for direct execution of <code>.dmb</code> files in UNIX. The most common use is for writing CGI programs that are executed by the web server.

The first parameter in the `executor` text string is the path to DreamDaemon. The one listed above is the standard UNIX location.

Optional parameters may follow. The most common are -CGI and -logself.


```dm

world/executor = "/usr/local/byond/bin/DreamDaemon -CGI -logself"

```


This example creates a CGI program to be executed by a web server. It puts its error output in the file <code>`projname`.log</code>.

All of this is configured for you when you include <code>html/CGI.dm</code> from the html library.
***