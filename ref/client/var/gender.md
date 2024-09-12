## gender var (client)
**See also:**
+   [New proc (client)](/ref/client/proc/New.md) 
+   [gender var (atom)](/ref/atom/var/gender.md) 
+   [key var (client)](/ref/client/var/key.md) 
+   [macros (text)](/ref/DM/text/macros.md) 

This is the client\'s gender, which is an attribute of the
player\'s key. By default, when a new mob is made for a player (in
client.New()), the new mob gets the same name and gender as the
player\'s key. This influences text macros like `\he`, which may expand
to \"it\", \"he\", \"she\", or \"they\". Valid values are+ 
```

\"neuter\" \"male\" \"female\" \"plural\" 
```
