
## cmptext (proc)

**Format:**
+   cmptext(T1,T2,...)

**Arguments:**
+   Any number of text strings to compare.

**Returns:**
+   1 if all arguments are equal; 0 otherwise.
***
This instruction is NOT sensitive to case. It also ignores the <code>\proper</code> and <code>\improper</code> text macros. The case-sensitive version is cmptextEx().


```dm

if(cmptext("Hi","HI"))
   world << "Equal!"
else
  world << "Not equal!"

```


This outputs "Equal!" since "Hi" and "HI" are the same, ignoring case.
***
**Related Pages:**
+    [cmptextEx proc](/ref/proc/cmptextEx)
