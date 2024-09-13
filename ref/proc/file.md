## file proc

**Format:**
+   file(Path)


Returns a file object corresponding to the named file. This
file object can then be used in a variety of ways. One would be to send
it to a player to view using the browse() instruction. Output may also
be appended to the file using the \<\< operator. 

Note that the
file exists in the external filesystem (ie the hard disk) and not the
cache. That means the path is specified in double quotes and will be
evaluated at run-time rather than compile-time. The file need not exist
at compile time and may even be modified at a later date. This is the
principle reason for using a file in the filesystem rather than a cached
resource file (specified in single quotes).
### Example:

``` dm
 mob/verb/help() usr \<\< browse(file(\"help.html\"))

```
 

Many DM instructions that deal with files treat
file(\"name\") and \"name\" the same. There are cases such as browse()
where a simple text string is not interpreted as a filename; it is in
those situations where file() is really necessary.

> [!TIP] 
> **See also:**
> +   [\<\< output operator](/ref/operator/%3c%3c/output.md) 
> +   [fcopy_rsc proc](/ref/proc/fcopy_rsc.md) 
> +   [ftp proc](/ref/proc/ftp.md) 
> +   [isfile proc](/ref/proc/isfile.md) 
> +   [link proc](/ref/proc/link.md) 
> +   [run proc](/ref/proc/run.md) 
> +   [savefile](/ref/savefile.md) 
> +   [sound proc](/ref/proc/sound.md) <!-- -->