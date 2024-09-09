[]{#/datum/proc/Write}    
## Write proc (datum)    
**See also:**    
:   [\<\< operator (savefile)](/ref/savefile/operator/%3c%3c/%3c%3c.md)    
:   [Read proc (datum)](/ref/datum/proc/Read/Read.md)    
:   [initial proc](/ref/proc/initial/initial.md)    
:   [issaved proc](/ref/proc/issaved/issaved.md)    
:   [tmp vars](/ref/var/tmp/tmp.md)    
<!-- -->    
**Format:**    
:   Write(savefile/F)    
<!-- -->    
**When:**    
:   Called when the object is written to a save file.    
<!-- -->    
**Args:**    
:   F: the save file being written to    
<!-- -->    
**Default action:**    
:   Write the value of each variable to a directory by the same name as    
    the variable. Variables marked tmp, global, or const and variables    
    which are equal to their initial value are skipped.  