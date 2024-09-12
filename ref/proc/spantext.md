## spantext proc 
###### BYOND Version 510
**See also:**
*   [findtext proc](/ref/proc/findtext.md) 
*   [nonspantext proc](/ref/proc/nonspantext.md) 
*   [splittext proc](/ref/proc/splittext.md) 
<!-- -->
**Format:**
*   spantext(Haystack,Needles,Start=1)
<!-- -->
**Returns:**
*   The number of consecutive characters, from the start position, that
    match the characters in Needles.
<!-- -->
**Args:**
*   Haystack* The text string to search.
*   Needles* A text string with all the characters that match.
*   Start* The text byte position in Haystack in which to begin the
    search.


This proc is case-sensitive. A common use for this proc is in
parsing. spantext(\"apples, oranges\",\", \",7) will tell you that,
starting at position 7, you need to skip 2 characters to get past any
commas or spaces. 

If the start position is negative, the
position is counted backwards from the end of the string. 

Note:
In strings containing non-ASCII characters, byte position and character
position are not the same thing. Use `spantext_char()` to work with
character counts instead of bytes, at a performance cost. See the
[Unicode](/ref/%7Bnotes%7D/Unicode.md) section for more information.