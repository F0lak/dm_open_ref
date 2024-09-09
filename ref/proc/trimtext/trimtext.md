[]{#/proc/trimtext}    
## trimtext proc {#trimtext-proc byondver="515"}    
**See also:**    
:   [copytext proc](ref/proc/copytext)    
<!-- -->    
**Format:**    
:   trimtext(Text)    
<!-- -->    
**Returns:**    
:   Text with whitespace trimmed from both ends    
<!-- -->    
**Args:**    
:   Text: The text string to trim.    
Trims whitespace from both ends of a text string.    
All [Unicode](ref/%7Bnotes%7D/Unicode) whitespace characters are counted,    
whether they can cause a break or not.  