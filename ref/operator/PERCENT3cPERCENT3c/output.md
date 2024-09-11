## \<\< output operator
**See also:**
*   [\<\< operator (savefile)](/ref/savefile/operator/%3c%3c.md) -m
*   [output proc](/ref/proc/output.md) -m
*   [browse proc](/ref/proc/browse.md) -m
*   [browse_rsc proc](/ref/proc/browse_rsc.md) -m
*   [file proc](/ref/proc/file.md) -m
*   [ftp proc](/ref/proc/ftp.md) -m
*   [image proc](/ref/proc/image.md) -m
*   [link proc](/ref/proc/link.md) -m
*   [load_resource proc](/ref/proc/load_resource.md) -m
*   [run proc](/ref/proc/run.md) -m
*   [sound proc](/ref/proc/sound.md) -m<!-- -->
**Format:**
*   A \<\< B


Cause the value B to be output to any players connected to mobs
specified in A. 

B may be an image, sound, or text. A may be a
mob, the whole world, or any list containing mobs.
### Example:

```
 usr \<\< \"Hi, \[usr.name\]\" view() \<\< \"To all in view\"
world \<\< \"Hi everybody!\" usr \<\< \'giggle.wav\' view() \<\<
image(/obj/Fireball,usr) 
```
