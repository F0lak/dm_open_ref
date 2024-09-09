[]{#/proc/EXCEPTION}    
## EXCEPTION proc    
**See also:**    
:   [try and catch statements](ref/proc/try)    
:   [throw statement](ref/proc/throw)    
:   [exception](ref/exception)    
:   [stddef.dm file](ref/%7B%7Bappendix%7D%7D/stddef%2edm)    
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