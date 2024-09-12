## shell proc
**See also:**
+   [fcopy proc](/ref/proc/fcopy.md) 
+   [fdel proc](/ref/proc/fdel.md) 
+   [file2text proc](/ref/proc/file2text.md) 
+   [process var (world)](/ref/world/var/process.md) 
+   [system_type var (world)](/ref/world/var/system_type.md) 
+   [text2file proc](/ref/proc/text2file.md) <!-- -->
**Format:**
+   shell(Command)
<!-- -->
**Args:**
+   Command+ system command to run
<!-- -->
**Returns:**
+   null on failure to execute command
+   exit code of command otherwise


This function is used to run an external program. The syntax of
Command depends on the server machine\'s operating system. Be sure to
redirect input and output to files if there is any. Also realize that
the command will fail if the program you try to run is not in the path
where the shell expects to find executable files (unless you specify a
full path). 

Since shell() allows arbitrary access to the
system, each call requires authorization from the person hosting the
world, unless running in trusted mode. Authorization is only sought when
running in Dream Seeker, since Dream Daemon is intended to be
non-interactive. Calling shell() with no arguments is a way of checking
if it is allowed by the current safety settings. It will return true if
running in Dream Seeker (regardless of safety mode) or if running in
Dream Daemon in trusted mode. 

The calling proc will sleep until
the command is finished executing.
### Example:

```
 mob/verb/dir(Path as text) shell(\"dir \[Path\] \> dir.out\")
usr \<\< file2text(\"dir.out\") 
```
 

This example
displays the output of the \"dir\" command to the user.