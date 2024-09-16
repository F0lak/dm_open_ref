## splittext proc 
###### BYOND Version 510

<!-- -->
**Format:**
+   splittext(Text,Delimiter,Start=1,End=0,include_delimiters=0)
<!-- -->
**Returns:**
+   A list of text strings split by the delimiter given.
<!-- -->
**Args:**
+   Text: The text string to search.
+   Delimiter: A text string that will be used as the separator between
    items, OR a regular expression (regex) used to find splits
+   Start: The text byte position in Text in which to begin looking for
    splits.
+   End: The text byte position in Text immediately following the last
    character to look at for splits.
+   include_delimiters: True if any delimiters found should be included
    in the result.


Splits up a text string and returns a list. The delimiter is
case-sensitive (unless you use a case-insensitive regular expression),
and can be more than one character long.
### Example:

``` dm
 var/list/items = splittext(\"apples,oranges,bananas\",
\",\") // prints \"apples\", \"oranges\", and \"bananas\" separately
for(var/item in items) usr \<\< item 
```
 

Where multiple
delimiters are next to each other, they\'re considered to be separating
an empty string. Therefore splittext(\"a,,b,c\", \",\") would return a
list with four elements instead of three. Splitting empty text returns
an empty list. 

If a regular expression is used as the
delimiter, any capturing groups in the expression will be included in
the list, in order. (The whole match itself will come first, if
include_delimiters is true.) So for instance splitting by regex(\",\")
will not include the comma, but splitting by regex(\"(,)\") will. Groups
that were not part of the match will be null. 

If the start or
end position is negative, the position is counted backwards from the end
of the string. Please note that the start and end positions do NOT trim
the string; if you want to split a trimmed string, trim it with
[copytext()](/ref/proc/copytext.md)  and send the result to
`splittext()` instead. 

Note: In strings containing non-ASCII
characters, byte position and character position are not the same thing.
Use `splittext_char()` to work with character counts instead of bytes,
at a performance cost. See the [Unicode](/ref/notes/Unicode.md) section
for more information.

> [!TIP] 
> **See also:**
> +   [findtext proc](/ref/proc/findtext.md) 
> +   [jointext proc](/ref/proc/jointext.md) 
> +   [nonspantext proc](/ref/proc/nonspantext.md) 
> +   [spantext proc](/ref/proc/spantext.md) 
> +   [Regular expressions](/ref/notes/regex.md) 