[]{#/proc/regex}
  ## regex proc {#regex-proc byondver="510"}
  **See also:**
  :   [Regular expressions](ref/%7Bnotes%7D/regex)
  :   [regex datum](ref/regex)
  :   [regex procs](ref/regex/proc)
  :   [findtext proc](ref/proc/findtext)
  :   [replacetext proc](ref/proc/replacetext)
  :   [splittext proc](ref/proc/splittext)
  :   [REGEX_QUOTE proc](ref/proc/REGEX_QUOTE)
  <!-- -->
  **Format:**
  :   regex(pattern, flags)
  :   regex(Regex)
  <!-- -->
  **Returns:**
  :   A new /regex datum.
  <!-- -->
  **Args:**
  :   pattern: The pattern string to search for
  :   flags: (optional) A text string containing any combination of
      modifier flags
  :   Regex: an existing /regex datum to copy
  Creates a [regular expression](ref/%7Bnotes%7D/regex), stored in a /regex
  datum, that can be used for searching and/or replacing text.