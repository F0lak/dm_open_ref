## parameters (skin)


Controls can be interacted with via
[winset()](/ref/proc/winset.md) {.code} and [winget()](/ref/proc/winset.md) {.code} to
change or read various parameters. 

Parameters come in a few
different formats:
-   Boolean* `true` or `false`
-   Numeric* any number, sometimes allowing decimal or negative numbers
-   String* text
-   Position* *x*`,`*y*
-   Size* *width*`x`*height*
-   Enumerated* one of several text choices, sometimes accepting numbers
    or true/false values as shortcuts


The list of [all controls](/ref/%7Bskin%7D/control.md) which shows
which parameters are universal, and each individual control type lists
additional parameters that apply to that type specifically.


Note* In any parameter\'s \"Applies to\" section, \"all\"
refers to positionable controls only, not Macro or Menu controls. Macro
and Menu will be listed separately if supported.