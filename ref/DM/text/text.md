[]{#/DM/text}
  ## text
  **See also:**
  :   [\<\< output operator](ref/operator/%3c%3c/output)
  :   [entities (text)](ref/DM/text/entities)
  :   [macros (text)](ref/DM/text/macros)
  :   [tags (text)](ref/DM/text/tags)
  :   [text proc](ref/proc/text)
  :   [Unicode](ref/%7Bnotes%7D/Unicode)
  Text consists of a string of characters enclosed in double quotes. To
  place a quote inside a string, escape it with a backslash `\` character.
  You will also need to escape a backslash if you want to use one on
  purpose.
  ### Example:
  usr \<\< \"He said, \\\"Hi.\\\"\"
  This example sends some text to the usr: `He said, "Hi."`
  Backslashes are also used for special [macros](ref/DM/text/macros) and to
  escape other characters that would normally be hard to include in a
  string. A backslash at the end of a line will ignore the line break, and
  continue the string on the next line after ignoring any leading spaces.
  To insert a variable expression into a string, enclose it in brackets
  `[]`. These are referred to as embedded text expressions. An object
  expression will display the object\'s name preceded by the text macro
  `\the` or `\The` if no other article has been specified. Capitalization
  of the article is inferred from context.
  ### Example:
  mob/verb/shout(T as text) world \<\< \"\[usr\]: \[T\]\"
  If this example is called by a mob named \"Bill\" with the text \"hi
  everybody!\", it will display \"Bill: hi everybody!\".
  On the other hand, if it is called by a mob named \"cat\", it would
  display \"The cat: hi everybody!\".
  Via [operator overloading](ref/operator/overload) you can define an
  `operator""` proc for an object to return different text when it\'s
  embedded in a string.
  ### Document strings
  For lengthy text strings, DM provides a special text *document* syntax.
  This begins with `{"` and ends with `"}`. It may include multiple lines
  and even un-escaped double quotes, but it still parses escape characters
  and embedded expressions.
  ### Example:
  mob/verb/end() usr \<\< {\" This is the way the world ends This is the
  way the world ends This is the way the world ends Not with a bang but a
  whimper. \--T.S. Eliot \"Hollow Men\" \"} del world //the end!
  ### Raw strings {#raw-strings byondver="512"}
  DM also has a format for raw strings, which do not allow escape
  characters or embedded expressions. This can be useful for many
  situations, especially [regular expressions](ref/%7Bnotes%7D/regex) which
  tend to use characters that need escaping. There are three ways to
  specify a raw string. All of them begin with the `@` character.
  Simple raw strings follow `@` with a single-character delimiter, usually
  `"` but it can be almost anything, and end when that delimiter is seen
  again. Line breaks are not allowed in simple raw strings.
  ### Examples:
  world \<\< @\"I can say \\ or \[\] without escaping anything!\" world
  \<\< @#Here I can use \"quotes\" but not the pound sign.# var/regex/R =
  new(@/(\\d+)/) // without raw strings world \<\< \"I can say \\\\ or
  \\\[\] without escaping anything!\" // lying world \<\< \"I have to
  escape \\\"quotes\\\" to use them.\" var/regex/R = new(\"(\\\\d+)\")
  Complex raw strings use more complicated delimiters, but they let you
  include line breaks. There are two ways to do this: One starts with
  `@{"` and ends with `"}`, so it looks like the familiar document string
  format. The other way starts with `@(XYZ)`, where `XYZ` is any arbitrary
  text you want it to be, and ends when that same text is encountered.
  With a complex raw string, a single leading and/or trailing line break
  will be ignored.
  ### Examples:
  world \<\< \@{\" Now I have absolute freedom to use \"quotes\" or
  \[brackets\] or line breaks, as long as I don\'t follow a quote with a
  closing brace. \"} world \<\< @(\~\~\~) Until three tilde (\~)
  characters are seen, this is a valid string. \~\~\~ // end of string
  world \<\< @(!!)You don\'t need a line break if you don\'t want one.!!