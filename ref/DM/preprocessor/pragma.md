[]{#/#pragma directive.md}    
## #pragma directive {#pragma-directive byondver="515"}    
**See also:**    
:   [#define directive]/DM/preprocessor/define    
:   [#include directive]/DM/preprocessor/include    
:   [preprocessor]/DM/preprocessor    
The `#pragma` directive alters the compiler\'s behavior in various ways.    
[#pragma multiple]/#pragma directive.md/multiple    
:   Include this file more than once.    
[#pragma ignore *Warning*]/#pragma directive.md/warn\    
[#pragma warn *Warning*]/#pragma directive.md/warn\    
[#pragma error *Warning*]/#pragma directive.md/warn    
:   Changes how the compiler handles certain warnings.    
[#pragma push]/#pragma directive.md/push    
:   Save the current pragma state.    
[#pragma pop]/#pragma directive.md/push    
:   Restore a previously saved warning state.    
[#pragma syntax]/#pragma directive.md/syntax    
:   Switch to a different syntax for parsing certain procs.    
[#pragma compatibility]/#pragma directive.md/compatibility    
:   Hint that the compiler should avoid using features higher than a    
    given version.    
[#pragma math]/#pragma directive.md/math    
:   Choose faster (old) or more accurate (new default) trigonometry.    
Pragmas will *not* be inherited by libraries included in your project.  