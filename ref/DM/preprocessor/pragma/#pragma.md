[]{#/DM/preprocessor/pragma}    
## #pragma directive {#pragma-directive byondver="515"}    
**See also:**    
:   [#define directive](/ref/DM/preprocessor/define/define.md)    
:   [#include directive](/ref/DM/preprocessor/include/include.md)    
:   [preprocessor](/ref/DM/preprocessor/preprocessor.md)    
The `#pragma` directive alters the compiler\'s behavior in various ways.    
[#pragma multiple](/ref/DM/preprocessor/pragma/multiple/multiple.md)    
:   Include this file more than once.    
[#pragma ignore *Warning*](/ref/DM/preprocessor/pragma/warn/warn.md)\    
[#pragma warn *Warning*](/ref/DM/preprocessor/pragma/warn/warn.md)\    
[#pragma error *Warning*](/ref/DM/preprocessor/pragma/warn/warn.md)    
:   Changes how the compiler handles certain warnings.    
[#pragma push](/ref/DM/preprocessor/pragma/push/push.md)    
:   Save the current pragma state.    
[#pragma pop](/ref/DM/preprocessor/pragma/push/push.md)    
:   Restore a previously saved warning state.    
[#pragma syntax](/ref/DM/preprocessor/pragma/syntax/syntax.md)    
:   Switch to a different syntax for parsing certain procs.    
[#pragma compatibility](/ref/DM/preprocessor/pragma/compatibility/compatibility.md)    
:   Hint that the compiler should avoid using features higher than a    
    given version.    
[#pragma math](/ref/DM/preprocessor/pragma/math/math.md)    
:   Choose faster (old) or more accurate (new default) trigonometry.    
Pragmas will *not* be inherited by libraries included in your project.  