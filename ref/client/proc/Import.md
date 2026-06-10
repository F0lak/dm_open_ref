
## Import (proc)

**Format:**
+   client.Import(Query)

**Arguments:**
+   Query: optional query parameters
***
When no query parameters are given, this returns the client-side file last exported with <code>client.Export()</code>. This comes as an entry in the resource cache, which can be opened as a savefile among other things. If there is no file, null is returned. For an example, see <a href="#/client/proc/Export">client.Export</a>.

When there are query parameters, these may be used to import a file from some alternate source. Currently this is not supported.
***
**Related Pages:**
+    [Export proc (client)](/ref/client/proc/Export)
+    [New proc (client)](/ref/client/proc/New)
+    [savefile](/ref/savefile)
