[]{#/text2ascii proc.md}    
## text2ascii proc    
**See also:**    
:   [ascii2text proc](/proc/ascii2text)    
:   [entities (text)](/DM/text/entities)    
:   [Unicode](/%7Bnotes%7D/Unicode)    
<!-- -->    
**Format:**    
:   text2ascii(T,pos=1)    
<!-- -->    
**Args:**    
:   T: A text string.    
:   pos: The byte position in T to use, starting at 1.    
<!-- -->    
**Returns:**    
:   A number representing the character\'s ASCII or Unicode code.    
ASCII codes are numerical values corresponding to keyboard and special    
characters. Among other things, they are used to represent many symbols    
in HTML. This proc converts a text string to its corresponding ascii    
representation.    
### Example:    
world \<\< text2ascii(\"A\") // = 65 world \<\< text2ascii(\"HAPPY\",2)    
// = 65    
With [Unicode](/%7Bnotes%7D/Unicode), things may get more complicated.    
DM stores text with UTF-8 encoding, so at this position there might be    
several bytes strung together to make a single character. The value of    
`pos` is in bytes, not characters. When the return value is 128 (0x80)    
or higher, multiple bytes are used for the charcter. In that case the    
next character position is not `pos + 1` like it is for regular text,    
but you can use `pos + length(ascii2text(result))` instead. Or, you can    
determine the byte count from this table:    
  Character code       Size in bytes    
  -------------------- ---------------    
  0 - 0x7F             1    
  0x80 - 0x7FF         2    
  0x800 - 0xFFFF       3    
  0x10000 - 0x10FFFF   4    
Alternatively, you can use `test2ascii_char()` to work with character    
positions instead of bytes, at a performance cost.  