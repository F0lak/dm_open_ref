
## browse (proc)

**Format:**
+   usr << browse(Body,Options)

**Arguments:**
+   Body: html text, file, or null to close the browser.
+   Options: optional parameters
***
This sends the html text or file to the user and optionally displays it in the web browser. The default action is to use the embedded browser panel in the Dream Seeker window; specifying an alternate window name (see below) causes it to appear in a popup window. Passing in 'null' for the html text causes the browser panel or named window to be closed.

The option parameters should either be omitted or they should be in a text string of the following format: <code> "`window`=name;`file`=name;`display`=1; <br/>`size`=300x300;`border`=0;`can_close`=1; <br/>`can_resize`=1;`can_minimize`=1;`titlebar`=1" </code>

You may use commas (,), ampersands (&amp;), or semicolons (;) as the delimiter. Any or all of the parameters may be specified and they may be included in any order.

Note also that many display options can be controlled through the html itself. For instance, to turn off the scrollbars, you can do: <code>&lt;body scroll=no&gt;</code>; to add a title, you can do: <code>&lt;head&gt;&lt;title&gt;My Title&lt;/title&gt;&lt;/head&gt;</code>; and so forth.

The following example displays a help page in a popup window.


```dm

var/const/help = {"

Help!


You are beyond help!



"}
client/verb/help()
   usr << browse(help,"window=help")

```

***
**Related Pages:**
+    [<< output operator](/ref/operator/%3c%3c/output)
+    [browse_rsc](/ref/proc/browse_rsc)
+    [file proc](/ref/proc/file)
+    [link proc](/ref/proc/link)
+    [run proc](/ref/proc/run)
+    [output proc](/ref/proc/output)
