## ftp proc
**See also:**
*   [\<\< output operator](/ref/operator/%3c%3c/output.md) -m
*   [browse proc](/ref/proc/browse.md) -m
*   [file proc](/ref/proc/file.md) -m
*   [link proc](/ref/proc/link.md) -m
*   [run proc](/ref/proc/run.md) -m
*   [sound proc](/ref/proc/sound.md) -m<!-- -->
**Format:**
*   target \<\< ftp(File, Name)


Sends a file to the target with the (optional) suggested name
for saving to disk. The file may be a cache file (loaded at compile
time) or an external file (accessed at run-time). Cache files are
specified in single quotes, and external files are in double quotes.


This function could be used to distribute source code,
supplementary documentation, or anything.
### Example:

```
 mob/verb/geticon(O in view()) usr \<\< ftp(O:icon) 
```



This example allows the user to download the icons from other
objects in the game.