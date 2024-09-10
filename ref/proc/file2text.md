[]{#/file2text proc.md}    
## file2text proc    
**See also:**    
:   [shell proc]/proc/shell    
:   [text2file proc]/proc/text2file    
<!-- -->    
**Format:**    
:   file2text(File)    
<!-- -->    
**Args:**    
:   File: file to read    
<!-- -->    
**Returns:**    
:   the contents of the file.    
This can be useful when interacting with external applications that    
generate output in a text file. For example, you might have an external    
program that mimics conversation:    
### Example:    
mob/oracle/verb/tell(T as text) text2file(T,\"talk.in\") shell(\"talk \<    
talk.in \> talk.out\") usr \<\< file2text(\"talk.out\")  