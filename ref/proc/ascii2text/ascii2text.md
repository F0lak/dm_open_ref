[]{#/proc/ascii2text}    
## ascii2text proc    
**See also:**    
:   [entities (text)](/ref/DM/text/entities.md)    
:   [text2ascii proc](/ref/proc/text2ascii.md)    
<!-- -->    
**Format:**    
:   ascii2text(N)    
<!-- -->    
**Returns:**    
:   A text string.    
<!-- -->    
**Args:**    
:   N: A number.    
ASCII codes are numerical values corresponding to keyboard and special    
characters. Among other things, they are used to represent many symbols    
in HTML. This proc converts an ASCII code to its corresponding text    
representation.    
### Example:    
T = ascii2text(65) // = \"A\"    
BYOND now supports [Unicode](/ref/%7Bnotes%7D/Unicode.md) via UTF-8 encoding,    
so you can use the character code for any valid Unicode character, not    
just ASCII.  