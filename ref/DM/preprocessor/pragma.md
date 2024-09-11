## #pragma directive 
###### BYOND Version 515
**See also:**
*   [#define directive](/ref/DM/preprocessor/define.md) -m
*   [#include directive](/ref/DM/preprocessor/include.md) -m
*   [preprocessor](/ref/DM/preprocessor.md) -m


The `#pragma` directive alters the compiler\'s behavior in
various ways.
[#pragma multiple](/ref/DM/preprocessor/pragma/multiple.md) -m
*   Include this file more than once.
[#pragma ignore *Warning*](/ref/DM/preprocessor/pragma/warn.md) -m\
[#pragma warn *Warning*](/ref/DM/preprocessor/pragma/warn.md) -m\
[#pragma error *Warning*](/ref/DM/preprocessor/pragma/warn.md) -m
*   Changes how the compiler handles certain warnings.
[#pragma push](/ref/DM/preprocessor/pragma/push.md) -m
*   Save the current pragma state.
[#pragma pop](/ref/DM/preprocessor/pragma/push.md) -m
*   Restore a previously saved warning state.
[#pragma syntax](/ref/DM/preprocessor/pragma/syntax.md) -m
*   Switch to a different syntax for parsing certain procs.
[#pragma compatibility](/ref/DM/preprocessor/pragma/compatibility.md) -m
*   Hint that the compiler should avoid using features higher than a
    given version.
[#pragma math](/ref/DM/preprocessor/pragma/math.md) -m*   Choose faster (old) or more accurate (new default) trigonometry.


Pragmas will *not* be inherited by libraries included in your
project.