[]{#/DM/preprocessor/pragma/syntax}    
## #pragma syntax directive {#pragma-syntax-directive byondver="516"}    
**See also:**    
:   [#pragma directive](ref/DM/preprocessor/pragma)    
:   [for loop proc](ref/proc/for/loop)    
:   [switch proc](ref/proc/switch)    
<!-- -->    
**Format:**    
:   #pragma syntax [\<]{.faded}C[\|]{.faded}DM[\>]{.faded}    
    [\[]{.faded}for[\|]{.faded}switch[\]]{.faded}    
Changes the syntax used to parse certain statements. This can be more    
natural for users who prefer non-DM style, and can sometimes do things    
that regular DM syntax can\'t do.    
Changing the [`for()` loop](ref/proc/for/loop) syntax to C will use    
semicolons to separate the Init, Test, Inc sections instead of commas.    
That means commas can be used to chain multiple statements together    
instead.    
In [switch()](ref/proc/switch){.code}, C syntax changes the if/else    
statements to use C\'s `case` and/or `default` keywords, followed by a    
colon, and the [`break` statement](ref/proc/break) is required to skip to    
the end of the switch unless you want to fall through to the next case.    
Fall-through behavior isn\'t possible in the default DM syntax.    
### Example:    
#pragma push #pragma syntax C switch switch(thing) case 1: usr \<\<    
\"This is case 1!\" break case 2, 3: usr \<\< \"This is case 2 or 3.\"    
// no break, fall through case 4 to 6: usr \<\< \"This is case 4 through    
6 (or maybe 2 or 3).\" break default: usr \<\< \"This is a different    
case. #pragma pop  