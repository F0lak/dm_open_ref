## text proc    
**See also:**    
:   [\<\< operator](/operator/%3c%3c)    
:   [macros (text)](/DM/text/macros)    
<!-- -->    
**Format:**    
:   text(FormatText,Args)    
<!-- -->    
**Returns:**    
:   The text with macros arguments substituted.    
<!-- -->    
**Args:**    
:   FormatText: a text string possibly containing text macros.    
:   Args: a set of arguments that corresponds to the number of empty    
    embedded expressions in FormatText.    
Complicated or lengthy embedded expressions in a text string can    
sometimes make the string difficult to read. In this case, one can use    
trailing arguments. The position in which the expression should be    
substituted should be marked with \[\] and the expression should then be    
passed as an argument after the text string.    
### Example:    
usr \<\< text(\"You are \[\] leagues from home.\",sqrt(usr.x\*\*2 +    
usr.y\*\*2))  