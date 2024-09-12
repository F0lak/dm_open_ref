## \_\_PROC\_\_ macro 
###### BYOND Version 515
**See also:**
*   [\_\_FILE\_\_ macro](/ref/DM/preprocessor/__FILE__.md) 
*   [\_\_LINE\_\_ macro](/ref/DM/preprocessor/__LINE__.md) 
*   [\_\_TYPE\_\_ macro](/ref/DM/preprocessor/__TYPE__.md) 
*   [\_\_IMPLIED_TYPE\_\_ macro](/ref/DM/preprocessor/__IMPLIED_TYPE__.md) 

The `__PROC__` macro is replaced by a reference to the current
proc being compiled. This may be useful when generating debugging error
messages, especially when wrapped in `nameof`, e.g. `nameof(__PROC__)`.


This is actually a pseudo-macro; the preprocessor doesn\'t
handle it directly.