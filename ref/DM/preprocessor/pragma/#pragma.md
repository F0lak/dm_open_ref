[]{#/DM/preprocessor/pragma}    
## #pragma directive {#pragma-directive byondver="515"}    
**See also:**    
:   [#define directive](/ref/DM/preprocessor/define)    
:   [#include directive](/ref/DM/preprocessor/include)    
:   [preprocessor](/ref/DM/preprocessor)    
The `#pragma` directive alters the compiler\'s behavior in various ways.    
[#pragma multiple](/ref/DM/preprocessor/pragma/multiple)    
:   Include this file more than once.    
[#pragma ignore *Warning*](/ref/DM/preprocessor/pragma/warn)\    
[#pragma warn *Warning*](/ref/DM/preprocessor/pragma/warn)\    
[#pragma error *Warning*](/ref/DM/preprocessor/pragma/warn)    
:   Changes how the compiler handles certain warnings.    
[#pragma push](/ref/DM/preprocessor/pragma/push)    
:   Save the current pragma state.    
[#pragma pop](/ref/DM/preprocessor/pragma/push)    
:   Restore a previously saved warning state.    
[#pragma syntax](/ref/DM/preprocessor/pragma/syntax)    
:   Switch to a different syntax for parsing certain procs.    
[#pragma compatibility](/ref/DM/preprocessor/pragma/compatibility)    
:   Hint that the compiler should avoid using features higher than a    
    given version.    
[#pragma math](/ref/DM/preprocessor/pragma/math)    
:   Choose faster (old) or more accurate (new default) trigonometry.    
Pragmas will *not* be inherited by libraries included in your project.  