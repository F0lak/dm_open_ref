[]{#/proc/ftime}    
## ftime proc    
**See also:**    
:   [time2text proc](/ref/proc/time2text/time2text.md)    
:   [flist proc](/ref/proc/flist/flist.md)    
:   [fexists proc](/ref/proc/fexists/fexists.md)    
:   [length proc](/ref/proc/length/length.md)    
<!-- -->    
**Format:**    
:   ftime(File, IsCreationTime)    
<!-- -->    
**Args:**    
:   File: name of file to test    
:   IsCreationTime (optional): true to return file creation time, false    
    (default) to return last-modified time    
<!-- -->    
**Returns:**    
:   A time value that can be sent to time2text().  