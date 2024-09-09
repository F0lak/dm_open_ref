[]{#/verb/set/hidden}    
## hidden setting (verb)    
**See also:**    
:   [category setting (verb)](ref/verb/set/category)    
:   [invisibility setting (verb)](ref/verb/set/invisibility)    
:   [name setting (verb)](ref/verb/set/name)    
:   [popup_menu setting (verb)](ref/verb/set/popup_menu)    
<!-- -->    
**Format:**    
:   set hidden = Setting    
<!-- -->    
**Args:**    
:   Setting: 1 for hidden verbs; 0 otherwise.    
A hidden verb is not visible to players (in menus or in expansion lists)    
but if typed in full can still be accessed.    
An alternate way to hide a verb from the command-line and verb panels is    
to make \".\" the first character in the name. The verb will not show up    
in command-expansion (ie when hitting spacebar) until the \".\" has been    
typed. This could be useful for hiding verbs that would otherwise    
clutter up the verb list, while still making them relatively easy to    
use. If you think this is a random quirky feature, you are right. To put    
\".\" in front of the name, use the [name setting](ref/verb/set/name).  