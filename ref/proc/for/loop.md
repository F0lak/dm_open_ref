## for loop proc

<!-- -->
**Format:**
+   for(Init, Test, Inc) Statement


First execute Init. Then if Test is true (non-zero), execute
Statement. After this execute Inc. Continue checking Test, doing
Statement, and performing Inc until Test turns out to be false (zero).


Statement may be a code block or a single statement. Semicolons
may be substituted for commas inside the parentheses as a convenience to
C/C++ programmers. 

Init and Inc may be omitted. If Test is
omitted, the loop will continue forever (unless a break, goto, or return
instruction is used to get out of the loop).
### Example:

``` dm
 var/i for(i=0, i\<3, i++) world \<\< i 
```



This outputs: 
``` dm
 0 1 2 
```
 

Note: An
Inc statement like `i += 0.1` is perfectly valid, but you should keep in
mind that numerical accuracy is not exact. See
[Numbers](/ref/notes/numbers.md)  for more information.
### C-like syntax


Using the [`#pragma syntax`
directive](/ref/DM/preprocessor/pragma/syntax.md) you can change `for()` to be
more like other languages such as C. This uses a semicolon `;` in place
of commas to separate Init, Test, and Inc. Instead the comma is treated
as a way of stringing multiple statements together.
### Example:

``` dm
 // make this syntax change temporary #pragma push #pragma
syntax C for var/i,j for(i=j=0; i\<=10; ++i,j+=i) world \<\< \"A
triangle \[i\] block\\s high has \[j\] block\\s total.\" #pragma pop

```


> [!TIP] 
> **See also:**
> +   [break statement](/ref/proc/break.md) 
> +   [continue statement](/ref/proc/continue.md) 
> +   [do proc](/ref/proc/do.md) 
> +   [for list proc](/ref/proc/for/list.md) 
> +   [while proc](/ref/proc/while.md) 