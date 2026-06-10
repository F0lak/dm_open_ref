
## args (var)
***
This is a list of the arguments passed to the proc or verb.


```dm

proc/add()
  var {cur; tot}
  for(cur in args)
    tot += cur
  return tot

```


Here, `add()` may be called with any number of arguments, each accessed through the `args` list.
***
**Related Pages:**
+    [list](/ref/list)
