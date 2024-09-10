[]{#/__TYPE__ macro.md}    
## \_\_TYPE\_\_ macro {#type__-macro byondver="515"}    
**See also:**    
:   [\_\_FILE\_\_ macro]/DM/preprocessor/__FILE__    
:   [\_\_LINE\_\_ macro]/DM/preprocessor/__LINE__    
:   [\_\_PROC\_\_ macro]/DM/preprocessor/__PROC__    
:   [\_\_IMPLIED_TYPE\_\_ macro]/DM/preprocessor/__IMPLIED_TYPE__    
The `__TYPE__` macro is replaced by a reference to the type path    
currently being compiled. This may be useful when generating debugging    
error messages. If used in a global proc, the value will be null.    
This is actually a pseudo-macro; the preprocessor doesn\'t handle it    
directly.  