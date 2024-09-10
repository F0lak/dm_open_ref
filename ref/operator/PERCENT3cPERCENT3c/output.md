[]{#/&lt;&lt; output operator.md}    
## \<\< output operator    
**See also:**    
:   [\<\< operator (savefile)](/savefile/operator/%3c%3c)    
:   [output proc](/proc/output)    
:   [browse proc](/proc/browse)    
:   [browse_rsc proc](/proc/browse_rsc)    
:   [file proc](/proc/file)    
:   [ftp proc](/proc/ftp)    
:   [image proc](/proc/image)    
:   [link proc](/proc/link)    
:   [load_resource proc](/proc/load_resource)    
:   [run proc](/proc/run)    
:   [sound proc](/proc/sound)    
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