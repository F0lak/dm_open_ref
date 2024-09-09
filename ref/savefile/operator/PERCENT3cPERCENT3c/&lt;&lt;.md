[]{#/savefile/operator/%3c%3c}    
## \<\< operator (savefile)    
**See also:**    
:   [\>\> operator (savefile)](ref/savefile/operator/%3e%3e)    
:   [\<\< output operator](ref/operator/%3c%3c/output)    
:   [Write proc (datum)](ref/datum/proc/Write)    
<!-- -->    
**Format:**    
:   F \<\< Val    
:   F\[\"Path\"\] \<\< Val    
Writes Val to a buffer. If Path is not specified, the current buffer    
will be used. Otherwise, the buffer at the specified path will be    
written to. Whenever the current directory is set, writing starts at the    
beginning of that buffer (replacing any previous contents). For this    
reason, when the Path parameter is given, the specified buffer is always    
overwritten.    
If Val is an object, a separate directory will be created for the object    
and the object\'s Write proc will be called. In addition to data that    
may be written by the Write() proc, the type of the object is stored in    
a buffer called \"type\". In the case of turfs, the location of the turf    
is also recorded so that it can be recreated at the same position. All    
other objects must be repositioned after the object is recreated (like    
in the object\'s Read() proc).    
Single operations that write multiple values (such as saving an object)    
are handled somewhat specially to avoid two references to the same    
object creating duplicate entries in the savefile. After the object    
being referenced is written once, successive references to the same    
object will be saved simply as references rather than as full objects.    
If this was not done, two references to the same object would be read    
back in as two separate objects. This also avoids infinite loops that    
would result when objects contain references back to themselves.  