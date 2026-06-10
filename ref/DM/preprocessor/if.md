
## if (info)

**Format:**
+   #if Val
+   ...
+   #elif Val2
+   ...
+   #else
+   ...
+   #endif

**Arguments:**
+   Val: A logical expression.
***
The <code>#if</code> statement is used to conditionally compile code. If Val is true (non-zero), the code following the <code>#if</code> statement will be compiled. Otherwise, compilation skips to the next <code>#elif</code>, <code>#else</code>, or <code>#endif</code> statement.

The function <code>defined()</code> can be used in the conditional expression. It is true if its argument is a defined macro (with <code>#define</code>) and false otherwise.


```dm

#if defined(DEBUG)
// This code will be compiled if DEBUG is
// defined
#else
// This code will be compiled if DEBUG is
// not defined
#endif

```


You can also use `fexists()` in a conditional to check if a file exists.
***
**Related Pages:**
+    [#define directive](/ref/DM/preprocessor/define)
+    [#ifdef directive](/ref/DM/preprocessor/ifdef)
