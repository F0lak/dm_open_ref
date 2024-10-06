## \#if directive

**Format:**
+   #if Val
+   ...
+   #elif Val2
+   ...
+   #else
+   ...
+   #endif

**Args:**
+   Val: A logical expression.

The `#if` statement is used to conditionally compile code. If
Val is true (non-zero), the code following the `#if` statement will be
compiled. Otherwise, compilation skips to the next `#elif`, `#else`, or
`#endif` statement. 

The function `defined()` can be used in the
conditional expression. It is true if its argument is a defined macro
(with `#define`) and false otherwise.
### Example:

```dm
#if defined(DEBUG)
// This code will be compiled if DEBUG is
// defined
#else
// This code will be compiled if DEBUG is
// not defined
#endif
```
 
You can also use `fexists()` in a
conditional to check if a file exists.

> [!TIP] 
> **See also:**
> +   [#define directive](/ref/DM/preprocessor/define.md) 
> +   [#ifdef directive](/ref/DM/preprocessor/ifdef.md) 