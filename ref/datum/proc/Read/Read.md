[]{#/datum/proc/Read}    
## Read proc (datum)    
**See also:**    
:   [\>\> operator (savefile)](/ref/savefile/operator/%3e%3e)    
:   [Write proc (datum)](/ref/datum/proc/Write)    
:   [tmp vars](/ref/var/tmp)    
<!-- -->    
**Format:**    
:   Read(savefile/F)    
<!-- -->    
**When:**    
:   Called when the object is read from a save file.    
<!-- -->    
**Args:**    
:   F: the save file being read    
<!-- -->    
**Default action:**    
:   Read the value of each variable from a directory by the same name as    
    the variable. Variables marked tmp, global, or const and variables    
    for which there is no directory are skipped.  