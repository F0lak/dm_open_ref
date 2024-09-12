## #warn directive

**Format:**
+   #warn Text
<!-- -->
**Args:**
+   Text: a warning message to display


The #warn directive displays the specified message as a
warning, but does not prevent the project from compiling.
### Example:

```
 #ifdef USE_LIGHTING #warn The lighting feature in MyLibrary
is experimental. #endif 
```


**See also:**
+   [preprocessor](/ref/DM/preprocessor.md) 
+   [#error directive](/ref/DM/preprocessor/error.md) <!-- -->