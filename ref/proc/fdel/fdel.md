[]{#/proc/fdel}    
## fdel proc    
**See also:**    
:   [shell proc](ref/proc/shell)    
<!-- -->    
**Format:**    
:   fdel(File)    
<!-- -->    
**Args:**    
:   File: name of file to delete    
<!-- -->    
**Returns:**    
:   1 on success; 0 otherwise.    
If the specified file ends in \'`/`\', it is treated as a directory. Any    
contents (including sub-directories) are deleted as well.    
Be careful!  