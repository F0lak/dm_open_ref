[]{#/DM/preprocessor/pragma/compatibility}    
## #pragma compatibility directive {#pragma-compatibility-directive byondver="516"}    
**See also:**    
:   [#pragma directive](/ref/DM/preprocessor/pragma)    
:   [warn/ignore/error directive](/ref/DM/preprocessor/warn)    
:   [DM_VERSION macro](/ref/DM/preprocessor/DM_VERSION)    
<!-- -->    
**Format:**    
:   #pragma compatibility [\<]{.faded}version[\>]{.faded}    
Hints that the compiler should avoid using features past a certain major    
BYOND version. If it encounters a situation where you explicitly or    
implicitly use a newer feature than requested, it will generate a    
warning.    
### Example:    
#pragma compatibility 515 A value of 0 or anything negative will reset    
the compatibility version to the default.  