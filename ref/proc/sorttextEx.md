## sorttextEx proc

**Format:**
+   sorttextEx(T1,T2,...)
<!-- -->
**Args:**
+   Any number of text strings to sort.
<!-- -->
**Returns:**
+   1 if text is ascending
+   -1 if text is descending
+   0 otherwise.


This instruction is sensitive to case. The case-insensitive
version is sorttext(). 

Note: Uppercase letters are lower in the
alphabetical order than lowercase letters.
### Example:

``` dm
 switch(sorttextEx("a","B")) if(1) world <<
"ascending" if(-1)world << "descending" if(0) world <<
"neither" 
```
 

This outputs, "descending", since
"B" comes before "a" in the alphabet.
Note: This proc used to be named `sortText`, like `sorttext` but with a
capital T. To avoid confusion it has been renamed, but old code will
still compile.

> [!TIP] 
> **See also:**
> +   [> operator](/ref/operator/%3e.md) 
> +   [< operator](/ref/operator/%3c.md) 
> +   [sorttext proc](/ref/proc/sorttext.md) <!-- -->