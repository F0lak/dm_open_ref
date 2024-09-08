[]{#/regex}
## regex datum {#regex-datum byondver="510"}
**See also:**
:   [Regular expressions](#/%7Bnotes%7D/regex)
:   [regex procs](#/regex/proc)
:   [regex vars](#/regex/var)
:   [regex proc](#/proc/regex)
:   [REGEX_QUOTE proc](#/proc/REGEX_QUOTE)
:   [findtext proc](#/proc/findtext)
:   [splittext proc](#/proc/splittext)
:   [stddef.dm file](#/%7B%7Bappendix%7D%7D/stddef%2edm)
The /regex datum holds a regular expression that can be used for
searching and/or replacing text. Rather than searching for a specific
piece of text, a regular expression is a *pattern* to search for. This
can include things like wildcards. See [Regular
expressions](#/%7Bnotes%7D/regex) for more information.
A new regular expression can be created with regex() or new/regex().