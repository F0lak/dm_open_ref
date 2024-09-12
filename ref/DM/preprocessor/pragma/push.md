## #pragma push/pop directive 
###### BYOND Version 515


`#pragma push` saves the current state any pragma flags, so for
instance a warning\'s level can be temporarily changed to ignore, warn,
or error. 

`#pragma pop` restores a previously saved pragma
state.
### Example:

```
 // temporarily ignore the unused_var warning #pragma push
#pragma ignore unused_var proc/GNDN() var/nothing // var defined but not
used #pragma pop 
```


**See also:**
+   [#pragma directive](/ref/DM/preprocessor/pragma.md) 
+   [#pragma warn/ignore/error directive](/ref/DM/preprocessor/pragma/warn.md) 