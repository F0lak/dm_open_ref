## \>\> operator (savefile)
**See also:**
+   [\>\> input operator](/ref/operator/%3e%3e/input.md) 
+   [\<\< operator (savefile)](/ref/savefile/operator/%3c%3c.md) 
+   [Read proc (datum)](/ref/datum/proc/Read.md) <!-- -->
**Format:**
+   F \>\> Var
+   F\[\"Path\"\] \>\> Var


Reads a value from a buffer into a variable. If Path is not
specified, the current buffer will be used. Otherwise, the buffer at the
specified path will be accessed. Whenever the current directory is set,
reading starts at the beginning of that buffer (replacing any previous
contents). For this reason, when the Path parameter is given, the first
value in the specified buffer is always read. If there is no data in the
buffer or the end of the buffer has been reached, null is returned.


If the value read is a previously written object, its own
directory will be opened and the object\'s Read proc will be called to
load any data that was written in the object\'s Write proc. 

If
the value read is a savefile (ie a savefile inside of a savefile), it is
treated a little differently. Instead of returning a savefile object, it
returns data cached in the world\'s rsc file. This is to give you
control over what file this data is copied into before it is opened as a
savefile. If you want to just open it up in a temporary file, do
something like this: 
```
 obj var savefile/myfile Read() . = ..()
//do the normal stuff if(myfile) //load data into a temporary file and
create savefile object myfile = new/savefile(myfile) 
```
