## Import proc (client)
**See also:**
*   [Export proc (client)](/ref/client/proc/Export.md) 
*   [New proc (client)](/ref/client/proc/New.md) 
*   [savefile](/ref/savefile.md) 
<!-- -->
**Format:**
*   client.Import(Query)
<!-- -->
**Args:**
*   Query* optional query parameters


When no query parameters are given, this returns the
client-side file last exported with `client.Export()`. This comes as an
entry in the resource cache, which can be opened as a savefile among
other things. If there is no file, null is returned. For an example, see
[client.Export](/ref/client/proc/Export.md)  

When there are query
parameters, these may be used to import a file from some alternate
source. Currently this is not supported.