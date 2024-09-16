## #pragma warn/ignore/error directive 
###### BYOND Version 515

<!-- -->
**Format:**
+   #pragma
    [<]{.faded}warn[\|]{.faded}ignore[\|]{.faded}error[>]{.faded}
    WarningName


Changes the way the compiler responds to warnings (except those
caused by the [`#warn` directive](/ref/DM/preprocessor/warn.md) ). The warning
name appears in the compiler output when the warning is generated.


Multiple warning names can be used in the same pragma,
separated by commas.
### Example:

``` dm
 // temporarily ignore the unused_var warning #pragma push
#pragma ignore unused_var proc/GNDN() var/nothing // var defined but not
used #pragma pop 
```
 

Here is a list of warnings that are
disabled by default, but can be turned on for linting purposes:
  Name            Description
  --------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  init_proc       A var in a very commonly used type, like `/turf` or `/atom` or `/datum`, is being initialized with an init proc. An example is `var/stuff[]` or `var/list/stuff = list(1,2,3)` which creates a list in a special internal proc because calling [New()](/ref/datum/proc/New.md) . Best practice is to not initialize the list until it\'s needed.
  frequent_call   A very commonly called proc such as [New()](/ref/datum/proc/New.md)  or [Del()](/ref/datum/proc/Del.md) has been overridden on a type that gets created or destroyed frequently, such as `/turf`, `/atom`, or `/datum`.

> [!TIP] 
> **See also:**
> +   [#pragma directive](/ref/DM/preprocessor/pragma.md) 
> +   [#warn directive](/ref/DM/preprocessor/warn.md) 
> +   [#error directive](/ref/DM/preprocessor/error.md) 