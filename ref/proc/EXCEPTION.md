## EXCEPTION proc
**See also:**
*   [try and catch statements](/ref/proc/try.md) -m
*   [throw statement](/ref/proc/throw.md) -m
*   [exception](/ref/exception.md) -m
*   [stddef.dm file](/ref/%7B%7Bappendix%7D%7D/stddef%2edm.md) -m<!-- -->
**Format:**
*   EXCEPTION(value)
<!-- -->
**Args:**
*   value* A text string (such as an error message) or other value
    identifying the exception.


This is used to create an /exception datum, and is shorthand
for calling new/exception(value, \_\_FILE\_\_, \_\_LINE\_\_). The value
you provide will be in exception.name.