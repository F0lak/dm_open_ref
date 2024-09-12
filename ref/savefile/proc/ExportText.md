## ExportText proc (savefile)

<!-- -->
**Format:**
+   savefile.ExportText(path=cd,file)
<!-- -->
**Args:**
+   path: the path to export
+   file: optional file to write to


Converts all or part of a savefile to a human readable text
format, similar in syntax to DM. If no file is specified, the savefile
text is returned as a text string instead of being written to a file.


The following example shows how to export and later import a
savefile. The user\'s mob is written into a directory with the same name
as their [ckey](/ref/mob/var/ckey.md) and the result is written to a text
file.
### Example:

```
 mob/verb/write() var/savefile/F = new() var/txtfile =
file(\"players/\[ckey\].txt\") F\[ckey\] \<\< usr fdel(txtfile)
F.ExportText(\"/\",txtfile) usr \<\< \"Your savefile looks like this:\"
usr \<\< \"
    [html_encode(file2text(txtfile))]
\" mob/verb/read() var/savefile/F = new() var/txtfile =
file(\"players/\[ckey\].txt\") F.ImportText(\"/\",txtfile) F\[ckey\]
\>\> usr 
```


> [!TIP] 
> **See also:**
> +   [ImportText proc (savefile)](/ref/savefile/proc/ImportText.md) 