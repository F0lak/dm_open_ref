
## arguments (proc)
***
The parameters to a proc are referred to as arguments. To define argument variables, place them inside the ()'s in the proc definition. A default value may be specified. Otherwise, arguments default to null.


```dm

proc/Sum(a,b)
  return a + b

```



```dm

proc/set_mob_desc(mob/M,desc="big and bad")
  M.desc = desc
  world << "The new desc for [M] is [desc]."

```


Note how the variable type may be specified. It is just like any other variable definition, except "<code>var/</code>" is implicit and does not need to be typed.
***
**Related Pages:**
+    [named arguments (proc)](/ref/proc/arguments/named)
+    [path operators](/ref/operator/path)
+    [arglist proc](/ref/proc/arglist)
+    [args list var (proc)](/ref/proc/var/args)
