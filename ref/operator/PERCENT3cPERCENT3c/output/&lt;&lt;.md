[]{#/operator/%3c%3c/output}    
## \<\< output operator    
**See also:**    
:   [\<\< operator (savefile)](/ref/savefile/operator/%3c%3c/%3c%3c.md)    
:   [output proc](/ref/proc/output/output.md)    
:   [browse proc](/ref/proc/browse/browse.md)    
:   [browse_rsc proc](/ref/proc/browse_rsc/browse_rsc.md)    
:   [file proc](/ref/proc/file/file.md)    
:   [ftp proc](/ref/proc/ftp/ftp.md)    
:   [image proc](/ref/proc/image/image.md)    
:   [link proc](/ref/proc/link/link.md)    
:   [load_resource proc](/ref/proc/load_resource/load_resource.md)    
:   [run proc](/ref/proc/run/run.md)    
:   [sound proc](/ref/proc/sound/sound.md)    
<!-- -->    
**Format:**    
:   A \<\< B    
Cause the value B to be output to any players connected to mobs    
specified in A.    
B may be an image, sound, or text. A may be a mob, the whole world, or    
any list containing mobs.    
### Example:    
usr \<\< \"Hi, \[usr.name\]\" view() \<\< \"To all in view\" world \<\<    
\"Hi everybody!\" usr \<\< \'giggle.wav\' view() \<\<    
image(/obj/Fireball,usr)  