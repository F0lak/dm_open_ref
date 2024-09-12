## Replace proc (regex) 
###### BYOND Version 510
**See also:**
+   [Regular expressions](/ref/%7Bnotes%7D/regex.md) 
+   [regex datum](/ref/regex.md) 
+   [Find proc (regex)](/ref/regex/proc/Find.md) 
+   [regex vars](/ref/regex/var.md) 
+   [regex proc](/ref/proc/regex.md) 
+   [replacetext proc](/ref/proc/replacetext.md) 
<!-- -->
**Format:**
+   Replace(haystack, replacement, Start=1, End=0)
<!-- -->
**Returns:**
+   The original haystack string with the first match replaced. If using
    the \"g\" flag, all matches are replaced.
<!-- -->
**Args:**
+   haystack: The text to be searched
+   replacement: A piece of text, OR a proc, that will be used to
    replace the match
+   Start: The start position (in bytes) to search; defaults to 1, or to
    src.next if this is a global pattern
+   End: The position of the byte after the end of the search; 0 is the
    end. The actual match is allowed to extend past End.


Finds the regular expression pattern within the \"haystack\"
text, and replaces the match with the given replacement value.


In a non-global expression (not using the \"g\" flag), the
values of src.index and src.next are set as they would be in a global
Find(). See the Find() proc for more info. 

Note: In strings
containing non-ASCII characters, byte position and character position
are not the same thing. Use `Replace_char()` to work with character
counts instead of bytes. See the [Unicode](/ref/%7Bnotes%7D/Unicode.md) section for more information.
### Replacing with text


If the replacement value is text, the \$ character is treated
as special. If you want to use the actual dollar sign, it must be
escaped with a second dollar sign. Otherwise, the \$ character is one of
these special values:
  Replacement         Value
  ------------------- -----------------------------------------------------------------------------------------
  \$1 *through* \$9   `$1`tt\> is whatever was in the first parentheses group, `$2` is the second, and so on.
  \$\`                The text that came before the match
  \$\'                The text that came after the match
  \$0 *or* \$&        The whole match itself
### Replacing with a proc


If replacing matches with a proc, then the proc will be called
with the match as its first argument, and any capturing groups as the
following arguments. Whatever the proc returns will be used as the
replacement text in place of the match.
### Example

```
 var/regex/vowels = new(\"\[aeiou\]\", \"i\") // match any
word of 2 letters or more var/regex/piglatin =
new(\"\\\\b(\\\\l)(\\\\l+)\\\\b\", \"ig\") // group1 is the first
letter, and group2 is everything else proc/word2piglatin(match, group1,
group2) // If the word starts with a vowel, just add \"ay\"
if(vowels.Find(group1)) return \"\[match\]ay\" // If the word was
capitalized, capitalize the replacement if(group1 == uppertext(group1))
group1 = lowertext(group1) group2 = uppertext(copytext(group2,1,2)) +
lowertext(copytext(group2,2)) return \"\[group2\]\[group1\]ay\"
mob/verb/PigSay(msg as text) msg = html_encode(msg) world \<\<
piglatin.Replace(msg, /proc/word2piglatin) 
```
