[]{#/entities (text).md}    
## entities (text)    
**See also:**    
:   [macros (text)]/DM/text/macros    
:   [tags (text)]/DM/text/tags    
:   [text]/DM/text    
Special characters may be inserted into text using HTML syntax. Such    
characters are known as entities. They start with an ampersand and end    
with a semicolon. The main reason for doing this is to insert characters    
that otherwise have a special meaning. The most common entities have    
names. The rest must be referred to by their Unicode character number    
(e.g. `&#38;` is the same as `&amp;`). The common ones are listed in the    
following table. Note that the same effect may be achieved by simply    
escaping the special character (like `\<`). The full entity syntax is    
included for generality.    
  Entity   Character    
  -------- -----------    
  &amp;    &    
  &lt;     \<    
  &gt;     \>    
  &quot;   \"    
  &copy;   ©    
When using numbered entities, you can put an `x` in front of the number    
to use hexadecimal. For instance `&#x26;`, `&#38;`, and `&amp;` are all    
equivalent.  