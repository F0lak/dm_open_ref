## #pragma directive 
###### BYOND Version 515



The `#pragma` directive alters the compiler\'s behavior in
various ways.
[#pragma multiple](/ref/DM/preprocessor/pragma/multiple.md) 
+   Include this file more than once.
[#pragma ignore *Warning*](/ref/DM/preprocessor/pragma/warn.md) \
[#pragma warn *Warning*](/ref/DM/preprocessor/pragma/warn.md) \
[#pragma error *Warning*](/ref/DM/preprocessor/pragma/warn.md) 
+   Changes how the compiler handles certain warnings.
[#pragma push](/ref/DM/preprocessor/pragma/push.md) 
+   Save the current pragma state.
[#pragma pop](/ref/DM/preprocessor/pragma/push.md) 
+   Restore a previously saved warning state.
[#pragma syntax](/ref/DM/preprocessor/pragma/syntax.md) 
+   Switch to a different syntax for parsing certain procs.
[#pragma compatibility](/ref/DM/preprocessor/pragma/compatibility.md) 
+   Hint that the compiler should avoid using features higher than a
    given version.
[#pragma math](/ref/DM/preprocessor/pragma/math.md) :   Choose faster (old) or more accurate (new default) trigonometry.


Pragmas will *not* be inherited by libraries included in your
project.

> [!TIP] 
> **See also:**
> +   [#define directive](/ref/DM/preprocessor/define.md) 
> +   [#include directive](/ref/DM/preprocessor/include.md) 
> +   [preprocessor](/ref/DM/preprocessor.md) 