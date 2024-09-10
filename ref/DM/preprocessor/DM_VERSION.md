[]{#/DM_VERSION macro.md}    
## DM_VERSION macro    
**See also:**    
:   [byond_version var (world)]/world/var/byond_version    
:   [byond_version var (client)]/client/var/byond_version    
:   [DM_BUILD macro]/DM/preprocessor/DM_BUILD    
:   [preprocessor]/DM/preprocessor    
:   [#pragma compatibility    
    directive]/DM/preprocessor/pragma/compatibility    
This macro indicates the version of the compiler. This could be useful    
when distributing code that uses new language features that would not    
compile in older compilers.    
### Example:    
#if DM_VERSION \< 230 #error This compiler is too far out of date!    
#endif    
If you use `#pragma compatibility`, it will alter the value of this    
macro (but never higher than the actual version being compiled). In this    
way you can alter your code\'s behavior based on the pragma.  