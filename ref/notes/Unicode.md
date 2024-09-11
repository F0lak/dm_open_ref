## Unicode 
###### BYOND Version 513
**See also:**
*   [text](/ref/DM/text.md) -m


BYOND was originally written to handle 8-bit (\"ANSI\")
characters only. However as time has marched on, Unicode has become
ubiquitous for supporting multiple languages, special characters, and
emojis. To adapt to this, BYOND now supports Unicode. 

When ANSI
was king, every character was exactly one byte in width, because the
only valid characters were between 1 and 255. (And technically, BYOND
reserved 255 for its own use.) Now, BYOND uses an encoding called UTF-8
to store characters that can\'t fit in one byte. 

UTF-8 breaks
up characters with codes of 128 or higher into multiple bytes, like so:
  Character code       Size in bytes
  -------------------- ---------------
  0 - 0x7F             1
  0x80 - 0x7FF         2
  0x800 - 0xFFFF       3
  0x10000 - 0x10FFFF   4
### Text handling


Importantly, BYOND\'s text procs are based on the byte
position, not the character position which may be lower. In other words,
`length("abcdéfg")` is greater than 7; it\'s 8, because `é` takes up 2
bytes in UTF-8. That also means `f` is at position 7, not position 6.


Why do the text procs work with byte position instead of
character position? Because ultimately, it\'s faster. Going by character
position would require counting every byte in a string (at least when it
uses UTF-8) until the right character position was found. This would be
detrimental to performance in most cases. 

For the most part,
this distinction should be fairly invisible to you. Most code isn\'t
going to encounter problems, but if you do a lot of text processing you
should be aware of it. 

In particular,
[text2ascii()](/ref/proc/text2ascii.md) -m.code} returns the Unicode value at a
specific position, which may cover several bytes. If you loop through a
string calling this proc for each character, you\'ll have to make
adjustments for cases when multiple bytes have been read. 

The
read-only `[]` index operator also uses byte positions. 

If you
read a byte or cut text at an inappropriate point, any broken characters
resulting from the cut will be turned into the Unicode replacement
character � which is 0xFFFD.
### `_char` procs


Most of the text handling procs have slower `_char` versions
(e.g., `copytext_char`) that use character positions instead of byte
positions. 

These should be used sparingly if at all; whenever
it\'s possible to use byte positions, you should. When you do use a
`_char` version of a proc, prefer using `-offset` instead of
`length_char(text)-offset` for positions near the end of the string.
Most text procs allow negative position values that count backwards from
the end, and counting a small number of characters backward is faster
than counting a lot of characters going forward.
### Old code


Code written in ANSI will be up-converted to UTF-8 by Dream
Maker, based on your current locale when the code is loaded.