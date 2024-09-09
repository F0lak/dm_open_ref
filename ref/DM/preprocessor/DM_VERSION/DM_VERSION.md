[]{#/DM/preprocessor/DM_VERSION}
  ## DM_VERSION macro
  **See also:**
  :   [byond_version var (world)](ref/world/var/byond_version)
  :   [byond_version var (client)](ref/client/var/byond_version)
  :   [DM_BUILD macro](ref/DM/preprocessor/DM_BUILD)
  :   [preprocessor](ref/DM/preprocessor)
  :   [#pragma compatibility
      directive](ref/DM/preprocessor/pragma/compatibility)
  This macro indicates the version of the compiler. This could be useful
  when distributing code that uses new language features that would not
  compile in older compilers.
  ### Example:
  #if DM_VERSION \< 230 #error This compiler is too far out of date!
  #endif
  If you use `#pragma compatibility`, it will alter the value of this
  macro (but never higher than the actual version being compiled). In this
  way you can alter your code\'s behavior based on the pragma.