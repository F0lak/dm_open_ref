
## group (var)
***
After a call to Find(), if this regular expression had any parentheses groups, whatever text was matched in those groups is stored here in a list.


```dm

var/regex/R = new("B(.)(.)(.)D")
R.Find("BYOND")     // find this pattern in "BYOND"

```

***
**Related Pages:**
+    [regex datum](/ref/regex)
+    [Find proc (regex)](/ref/regex/proc/Find)
+    [index var (regex)](/ref/regex/var/index)
+    [match var (regex)](/ref/regex/var/match)
