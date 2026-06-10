
## error (info)

**Format:**
+   #error Text

**Arguments:**
+   Text: an error message to display
***
The #error directive halts compilation and displays the specified message.


```dm

#if DM_VERSION < 4
#error This compiler is too far out of date!
#endif

```

***
**Related Pages:**
+    [preprocessor](/ref/DM/preprocessor)
+    [#warn directive](/ref/DM/preprocessor/warn)
