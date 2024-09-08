[]{#/savefile/proc/ImportText}
## ImportText proc (savefile)
**See also:**
:   [ExportText proc (savefile)](#/savefile/proc/ExportText)
<!-- -->
**Format:**
:   savefile.ImportText(path=cd,source)
<!-- -->
**Args:**
:   path: the path at which to write the imported data
:   source: a file or text string to import
Reads a text file or string and writes it into a savefile. See
[ExportText](#/savefile/proc/ExportText) for an example.
If `source` is an ordinary string, it will be treated as savefile
contents to be parsed. If it\'s a `file()` reference, it will be treated
as a filename and the file\'s contents will be loaded.