
## GetAPI (proc)

**Format:**
+   GetAPI(Api, Name)

**Arguments:**
+   Api: the name of the API (e.g. "steam")
+   Key: the name of the value to read
***
Interfaces with supported external APIs to read information. Currently this only has meaning for Steam, for specially built games that have a Steam app ID.

This proc returns null any time the call or its results are invalid: for instance, trying to query a Steam stat from a user who isn't logged into Steam.
***
**Related Pages:**
+    [SetAPI proc (client)](/ref/client/proc/SetAPI)
+    [CheckPassport proc (client)](/ref/client/proc/CheckPassport)
