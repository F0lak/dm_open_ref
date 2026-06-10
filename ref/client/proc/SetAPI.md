
## SetAPI (proc)

**Format:**
+   SetAPI(Api, Key, Value)

**Arguments:**
+   Api: the name of the API (e.g. "steam")
+   Key: the name of the value to change
+   Value: the new value to set
***
Interfaces with supported external APIs to write information. Currently this only has meaning for Steam, for specially built games that have a Steam app ID.

This proc returns null any time the call or its results are invalid.
***
**Related Pages:**
+    [GetAPI proc (client)](/ref/client/proc/GetAPI)
+    [CheckPassport proc (client)](/ref/client/proc/CheckPassport)
