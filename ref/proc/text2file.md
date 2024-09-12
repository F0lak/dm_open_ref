## text2file proc
**See also:**
*   [file2text proc](/ref/proc/file2text.md) 
*   [shell proc](/ref/proc/shell.md) <!-- -->
**Format:**
*   text2file(Text,File)
<!-- -->
**Args:**
*   Text* text to be added to file
*   File* file to be appended to
<!-- -->
**Returns:**
*   1 on success; 0 otherwise.


Appends text to a file. If the file does not exist, one will be
created. 

This can be useful when interacting with external
applications that read output from a text file. For example, you might
have an external program that mimics conversation:
### Example:

```
 mob/oracle/verb/tell(T as text) text2file(T,\"oracle.in\")
shell(\"oracle \< oracle.in \> oracle.out\") usr \<\<
file2text(\"oracle.out\") 
```
