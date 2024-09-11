## splicetext proc 
###### BYOND Version 514
**See also:**
*   [copytext proc](/ref/proc/copytext.md) -m
*   [Splice proc (list)](/ref/list/proc/Splice.md) -m
<!-- -->
**Format:**
*   splicetext(Text,Start=1,End=0,Insert=\"\")
<!-- -->
**Returns:**
*   Spliced text
<!-- -->
**Args:**
*   Text* The text string to splice.
*   Start* The text byte position in Text where the splice will begin.
*   End* The text byte position in Text immediately following the last
    character to be cut from the splice. 0 is the end of the string.
*   Insert* Text to be inserted.


Cuts out a section of a text string and inserts a different
piece of text in its place. This is basically equivalent to
`copytext(Text,1,Start) + Insert + copytext(Text,End)`, but faster.
### Example:

```
 // cuts \"nan\" from \"banana\" and replaces it with
\"laclav\" // prints \"balaclava\" usr \<\< splicetext(\"banana\", 3, 6,
\"laclav\") 
```
 

The `Start` and `End` index values can
be negative, which count backwards from the end of the string. If the
index values are out of range, there will be no error; they will simply
be clamped to the beginning or end of the string. If `End` comes before
`Start`, the two values are swapped. 

Note* In strings
containing non-ASCII characters, byte position and character position
are not the same thing. Use `splicetext_char()` to work with character
counts instead of bytes, at a performance cost. See the
[Unicode](/ref/%7Bnotes%7D/Unicode.md) -msection for more information.