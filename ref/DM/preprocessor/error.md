## #error directive
**See also:**
*   [preprocessor](/ref/DM/preprocessor.md) -m
*   [#warn directive](/ref/DM/preprocessor/warn.md) -m<!-- -->
**Format:**
*   #error Text
<!-- -->
**Args:**
*   Text* an error message to display


The #error directive halts compilation and displays the
specified message.
### Example:

```
 #if DM_VERSION \< 4 #error This compiler is too far out of
date! #endif 
```
