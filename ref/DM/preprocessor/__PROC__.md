
## __PROC__ (info)
***
The `__PROC__` macro is replaced by a reference to the current proc being compiled. This may be useful when generating debugging error messages, especially when wrapped in `nameof`, e.g. `nameof(__PROC__)`.

This is actually a pseudo-macro; the preprocessor doesn't handle it directly.
***
**Related Pages:**
+    [__FILE__ macro](/ref/DM/preprocessor/__FILE__)
+    [__LINE__ macro](/ref/DM/preprocessor/__LINE__)
+    [__TYPE__ macro](/ref/DM/preprocessor/__TYPE__)
+    [__IMPLIED_TYPE__ macro](/ref/DM/preprocessor/__IMPLIED_TYPE__)
