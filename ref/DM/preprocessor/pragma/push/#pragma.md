[]{#/DM/preprocessor/pragma/push}    
## #pragma push/pop directive {#pragma-pushpop-directive byondver="515"}    
**See also:**    
:   [#pragma directive](ref/DM/preprocessor/pragma)    
:   [#pragma warn/ignore/error directive](ref/DM/preprocessor/pragma/warn)    
`#pragma push` saves the current state any pragma flags, so for instance    
a warning\'s level can be temporarily changed to ignore, warn, or error.    
`#pragma pop` restores a previously saved pragma state.    
### Example:    
// temporarily ignore the unused_var warning #pragma push #pragma ignore    
unused_var proc/GNDN() var/nothing // var defined but not used #pragma    
pop  