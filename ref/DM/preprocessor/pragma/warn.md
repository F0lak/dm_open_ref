
## warn (info)

**Format:**
+   #pragma warnignoreerror WarningName
***
Changes the way the compiler responds to warnings (except those caused by the <a href="#/DM/preprocessor/warn">`#warn` directive</a>). The warning name appears in the compiler output when the warning is generated.

Multiple warning names can be used in the same pragma, separated by commas.


```dm

// temporarily ignore the unused_var warning
#pragma push
#pragma ignore unused_var

proc/GNDN()
    var/nothing // var defined but not used

#pragma pop

```


Here is a list of warnings that are disabled by default, but can be turned on for linting purposes:
***
**Related Pages:**
+    [#pragma directive](/ref/DM/preprocessor/pragma)
+    [#warn directive](/ref/DM/preprocessor/warn)
+    [#error directive](/ref/DM/preprocessor/error)
