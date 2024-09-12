## run proc

**Format:**
+   O \<\< run(File)


This is similar to link() but instead of a URL, you can pass a
file to be viewed directly. The file may be a cache file or an external
file.
### Example:

```
 mob/var/picture = \'mob.jpg\' mob/verb/view_pic(mob/M as mob
in view()) usr \<\< run(M.picture) mob/verb/set_pic(F as file)
usr.picture = F 
```
 

This example defines a picture to be
associated with each mob and a verb for viewing another mob\'s picture.
Players can also configure their own pictures.

**See also:**
+   [\<\< output operator](/ref/operator/%3c%3c/output.md) 
+   [file proc](/ref/proc/file.md) 
+   [link proc](/ref/proc/link.md) <!-- -->