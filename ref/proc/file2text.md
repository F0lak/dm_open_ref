## file2text proc

**Format:**
+   file2text(File)
<!-- -->
**Args:**
+   File: file to read
<!-- -->
**Returns:**
+   the contents of the file.


This can be useful when interacting with external applications
that generate output in a text file. For example, you might have an
external program that mimics conversation:
### Example:

```
 mob/oracle/verb/tell(T as text) text2file(T,\"talk.in\")
shell(\"talk \< talk.in \> talk.out\") usr \<\< file2text(\"talk.out\")

```


> [!TIP] 
> **See also:**
> +   [shell proc](/ref/proc/shell.md) 
> +   [text2file proc](/ref/proc/text2file.md) <!-- -->