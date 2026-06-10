
## cmptextEx (proc)

**Format:**
+   cmptextEx(T1,T2,...)

**Arguments:**
+   Any number of text strings to compare.

**Returns:**
+   1 if all arguments are equal; 0 otherwise.
***
This instruction is sensitive to case. The case-insensitive version is cmptext().

Because identical text is internally combined to conserve memory, cmptextEx(T1,T2) is equivalent to (T1 == T2).


```dm

if(cmptextEx("Hi","HI"))
   world << "Equal!"
else
  world << "Not equal!"

```


This outputs "Not equal!" since "Hi" and "HI" are different when taking case into account.


> [!TIP]
> Note: This proc used to be named cmpText, like cmptext but with a capital T. To avoid confusion it has been renamed, but old code will still compile.
***
**Related Pages:**
+    [cmptext proc](/ref/proc/cmptext)
