# preprocessor


The preprocessor performs various transformations on source
code as the DM compiler reads the file. It may be used to define
macros---that is words which are replaced by other fragments of code. It
is also possible to insert other source code files and to conditionally
compile or not compile sections of code. 

Preprocessor commands
are called directives. They are placed on a line by themselves and
always begin with a hash symbol `#`. The preprocessor directives
recognized by DM are the same as standard C compilers:
    #define
    #if
    #elif
    #ifdef
    #ifndef
    #else
    #endif
    #include
    #pragma
    #error
    #warn

> [!TIP] 
> 