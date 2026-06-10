
## cd (var)
***
This is the path name of the current directory. Setting it causes the current directory to change. (We are talking about the current <em>database</em> directory inside the savefile. It is not a real directory on the filesystem.) It is perfectly legal to change to a non-existent directory. This new directory will not be saved to disk unless its buffer (or one of its children) is modified, however.


```dm

var/savefile/F = new()  // temporary file

F.cd = "/MyDir/Icon"
F.cd = ".."    // change to /MyDir
F.cd = "Icon"  // change to /MyDir/Icon

```

***
**Related Pages:**
+    [savefile](/ref/savefile)
