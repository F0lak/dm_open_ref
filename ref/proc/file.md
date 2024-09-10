[]{#/file proc.md}    
## file proc    
**See also:**    
:   [\<\< output operator]/operator/%3c%3c/output    
:   [fcopy_rsc proc]/proc/fcopy_rsc    
:   [ftp proc]/proc/ftp    
:   [isfile proc]/proc/isfile    
:   [link proc]/proc/link    
:   [run proc]/proc/run    
:   [savefile]/savefile    
:   [sound proc]/proc/sound    
<!-- -->    
**Format:**    
:   file(Path)    
Returns a file object corresponding to the named file. This file object    
can then be used in a variety of ways. One would be to send it to a    
player to view using the browse() instruction. Output may also be    
appended to the file using the \<\< operator.    
Note that the file exists in the external filesystem (ie the hard disk)    
and not the cache. That means the path is specified in double quotes and    
will be evaluated at run-time rather than compile-time. The file need    
not exist at compile time and may even be modified at a later date. This    
is the principle reason for using a file in the filesystem rather than a    
cached resource file (specified in single quotes).    
### Example:    
mob/verb/help() usr \<\< browse(file(\"help.html\"))    
Many DM instructions that deal with files treat file(\"name\") and    
\"name\" the same. There are cases such as browse() where a simple text    
string is not interpreted as a filename; it is in those situations where    
file() is really necessary.  