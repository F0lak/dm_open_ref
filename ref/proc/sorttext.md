
## sorttext (proc)

**Format:**
+   sorttext(T1,T2,...)

**Arguments:**
+   Any number of text strings to sort.

**Returns:**
+   1 if text is ascending
+   -1 if text is descending
+   0 otherwise
***
This instruction is NOT sensitive to case. The case sensitive version is sorttextEx().


```dm

switch(sorttext("A","B"))
  if(1) world << "ascending"
  if(-1)world << "descending"
  if(0) world << "neither"

```


This outputs "ascending", since "A" comes before "B" in the alphabet.
***
**Related Pages:**
+    [> operator](/ref/operator/%3e)
+    [< operator](/ref/operator/%3c)
+    [sorttextEx proc](/ref/proc/sorttextEx)
