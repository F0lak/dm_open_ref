[]{#/proc/EXCEPTION}
## EXCEPTION proc
**See also:**
:   [try and catch statements](#/proc/try)
:   [throw statement](#/proc/throw)
:   [exception](#/exception)
:   [stddef.dm file](#/%7B%7Bappendix%7D%7D/stddef%2edm)
<!-- -->
**Format:**
:   EXCEPTION(value)
<!-- -->
**Args:**
:   value: A text string (such as an error message) or other value
    identifying the exception.
This is used to create an /exception datum, and is shorthand for calling
new/exception(value, \_\_FILE\_\_, \_\_LINE\_\_). The value you provide
will be in exception.name.