## #ifndef directive
**See also:**
+   [#define directive](/ref/DM/preprocessor/define.md) 
+   [#if directive](/ref/DM/preprocessor/if.md) 
+   [#ifdef directive](/ref/DM/preprocessor/ifdef.md) 
+   [preprocessor](/ref/DM/preprocessor.md) <!-- -->
**Format:**
+   #ifndef Name
<!-- -->
**Args:**
+   Name: A macro definition.


The `#ifndef` statement is used to conditionally compile code.
It is equivalent to `#if !defined(Name)`.