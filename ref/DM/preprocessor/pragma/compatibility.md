
## compatibility (info)

**Format:**
+   #pragma compatibility version
***
Hints that the compiler should avoid using features past a certain major BYOND version. If it encounters a situation where you explicitly or implicitly use a newer feature than requested, it will generate a warning.


```dm

#pragma compatibility 515

```


This directive also alters the <a class="code" href="#/DM/preprocessor/DM_VERSION">DM_VERSION</a> macro.

A value of 0 or anything negative will reset the compatibility version to the default.
***
**Related Pages:**
+    [#pragma directive](/ref/DM/preprocessor/pragma)
+    [#warn directive](/ref/DM/preprocessor/warn)
+    [DM_VERSION macro](/ref/DM/preprocessor/DM_VERSION)
