
## gender (var)
***
This is the client's gender, which is an attribute of the player's key. By default, when a new mob is made for a player (in client.New()), the new mob gets the same name and gender as the player's key. This influences text macros like <code>\he</code>, which may expand to "it", "he", "she", or "they". Valid values are:


```dm

"neuter"
"male"
"female"
"plural"

```

***
**Related Pages:**
+    [New proc (client)](/ref/client/proc/New)
+    [gender](/ref/atom/var/gender)
+    [key var (client)](/ref/client/var/key)
+    [macros (text)](/ref/DM/text/macros)
