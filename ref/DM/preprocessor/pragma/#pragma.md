[]{#/DM/preprocessor/pragma}
## #pragma directive {#pragma-directive byondver="515"}
**See also:**
:   [#define directive](#/DM/preprocessor/define)
:   [#include directive](#/DM/preprocessor/include)
:   [preprocessor](#/DM/preprocessor)
The `#pragma` directive alters the compiler\'s behavior in various ways.
[#pragma multiple](#/DM/preprocessor/pragma/multiple)
:   Include this file more than once.
[#pragma ignore *Warning*](#/DM/preprocessor/pragma/warn)\
[#pragma warn *Warning*](#/DM/preprocessor/pragma/warn)\
[#pragma error *Warning*](#/DM/preprocessor/pragma/warn)
:   Changes how the compiler handles certain warnings.
[#pragma push](#/DM/preprocessor/pragma/push)
:   Save the current pragma state.
[#pragma pop](#/DM/preprocessor/pragma/push)
:   Restore a previously saved warning state.
[#pragma syntax](#/DM/preprocessor/pragma/syntax)
:   Switch to a different syntax for parsing certain procs.
[#pragma compatibility](#/DM/preprocessor/pragma/compatibility)
:   Hint that the compiler should avoid using features higher than a
    given version.
[#pragma math](#/DM/preprocessor/pragma/math)
:   Choose faster (old) or more accurate (new default) trigonometry.
Pragmas will *not* be inherited by libraries included in your project.