## #pragma compatibility directive 
###### BYOND Version 516

**Format:**
+   #pragma compatibility \<version>

Hints that the compiler should avoid using features past a
certain major BYOND version. If it encounters a situation where you
explicitly or implicitly use a newer feature than requested, it will
generate a warning.
### Example:

```dm
 #pragma compatibility 515 
```
 A value of 0 or
anything negative will reset the compatibility version to the default.

> [!TIP] 
> **See also:**
> +   [#pragma directive](/ref/DM/preprocessor/pragma.md) 
> +   [warn/ignore/error directive](/ref/DM/preprocessor/warn.md) 
> +   [DM_VERSION macro](/ref/DM/preprocessor/DM_VERSION.md) 