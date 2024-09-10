[]{#/#pragma warn_ignore_error directive.md}    
## #pragma warn/ignore/error directive {#pragma-warnignoreerror-directive byondver="515"}    
**See also:**    
:   [#pragma directive](/DM/preprocessor/pragma)    
:   [#warn directive](/DM/preprocessor/warn)    
:   [#error directive](/DM/preprocessor/error)    
<!-- -->    
**Format:**    
:   #pragma    
    [\<]{.faded}warn[\|]{.faded}ignore[\|]{.faded}error[\>]{.faded}    
    WarningName    
Changes the way the compiler responds to warnings (except those caused    
by the [`#warn` directive](/DM/preprocessor/warn)). The warning name    
appears in the compiler output when the warning is generated.    
Multiple warning names can be used in the same pragma, separated by    
commas.    
### Example:    
// temporarily ignore the unused_var warning #pragma push #pragma ignore    
unused_var proc/GNDN() var/nothing // var defined but not used #pragma    
pop    
Here is a list of warnings that are disabled by default, but can be    
turned on for linting purposes:    
  Name            Description    
  --------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
  init_proc       A var in a very commonly used type, like `/turf` or `/atom` or `/datum`, is being initialized with an init proc. An example is `var/stuff[]` or `var/list/stuff = list(1,2,3)` which creates a list in a special internal proc because calling [New()](/datum/proc/New){.code}. Best practice is to not initialize the list until it\'s needed.    
  frequent_call   A very commonly called proc such as [New()](/datum/proc/New){.code} or [Del()](/datum/proc/Del){.code} has been overridden on a type that gets created or destroyed frequently, such as `/turf`, `/atom`, or `/datum`.  