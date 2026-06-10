
## warn (info)

**Format:**
+   #warn Text

**Arguments:**
+   Text: a warning message to display
***
The #warn directive displays the specified message as a warning, but does not prevent the project from compiling.


```dm

#ifdef USE_LIGHTING
#warn The lighting feature in MyLibrary is experimental.
#endif

```

***
**Related Pages:**
+    [preprocessor](/ref/DM/preprocessor)
+    [#error directive](/ref/DM/preprocessor/error)
