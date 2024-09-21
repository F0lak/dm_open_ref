## DM_VERSION macro

This macro indicates the version of the compiler. This could be
useful when distributing code that uses new language features that would
not compile in older compilers.
### Example:

``` dm
#if DM_VERSION < 230
#error This compiler is too far out of date!
#endif
```
 
If you use `#pragma compatibility`,
it will alter the value of this macro (but never higher than the actual
version being compiled). In this way you can alter your code\'s behavior
based on the pragma.

> [!TIP] 
> **See also:**
> +   [byond_version var (world)](/ref/world/var/byond_version.md) 
> +   [byond_version var (client)](/ref/client/var/byond_version.md) 
> +   [DM_BUILD macro](/ref/DM/preprocessor/DM_BUILD.md) 
> +   [preprocessor](/ref/DM/preprocessor.md) 
> +   [#pragma compatibility