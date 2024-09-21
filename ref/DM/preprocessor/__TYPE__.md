## \_\_TYPE\_\_ macro 
###### BYOND Version 515

The `__TYPE__` macro is replaced by a reference to the type
path currently being compiled. This may be useful when generating
debugging error messages. If used in a global proc, the value will be
null. 

This is actually a pseudo-macro; the preprocessor
doesn\'t handle it directly.

> [!TIP] 
> **See also:**
> +   [\_\_FILE\_\_ macro](/ref/DM/preprocessor/__FILE__.md) 
> +   [\_\_LINE\_\_ macro](/ref/DM/preprocessor/__LINE__.md) 
> +   [\_\_PROC\_\_ macro](/ref/DM/preprocessor/__PROC__.md) 
> +   [\_\_IMPLIED_TYPE\_\_ macro](/ref/DM/preprocessor/__IMPLIED_TYPE__.md) 