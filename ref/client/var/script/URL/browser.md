
## browser (var)
***
DM Script can be used to effectively make a hyperlink in a web document to a BYOND world. This is done by making a DM Script file that defines the desired URL. It need do nothing more than that. When a user clicks on the link in a web browser, DreamSeeker will pop up, execute the script, and connect to the specified URL.

Some browsers may need to be configured to know what to do with a DM Script file. For example, in Netscape, you can add an entry to the list of helper applications. You should add a MIME type called '<code>application/x-dms</code>' with the description 'DM Script' and the extension <code>dms</code>. Have this execute DreamSeeker with the <code>.dms</code> file as an argument.


```dm

/*If your browser shows you this, you either need
  to install BYOND (it's free!) from www.byond.com,
  or you need to configure your browser to execute
  DreamSeeker with DM Script (.dms) files.
*/
#define URL "byond://myworld"

```



```dm


Welcome to My World

You can connect to my world
here.




```


You can connect to my world <a href="myworld.dms">here</a>.
***
**Related Pages:**
+    [URL (client script)](/ref/client/var/script/URL)
