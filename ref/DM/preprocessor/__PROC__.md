## \_\_PROC\_\_ macro 
###### BYOND Version 515
**See also:**
*   [\_\_FILE\_\_ macro](/DM/preprocessor/__FILE__)
*   [\_\_LINE\_\_ macro](/DM/preprocessor/__LINE__)
*   [\_\_TYPE\_\_ macro](/DM/preprocessor/__TYPE__)
*   [\_\_IMPLIED_TYPE\_\_ macro](/DM/preprocessor/__IMPLIED_TYPE__)


The `__PROC__` macro is replaced by a reference to the current
proc being compiled. This may be useful when generating debugging error
messages, especially when wrapped in `nameof`, e.g. `nameof(__PROC__)`.


This is actually a pseudo-macro; the preprocessor doesn\'t
handle it directly.