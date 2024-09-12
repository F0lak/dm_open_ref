## savefile
**See also:**
+   [\>\> operator (savefile)](/ref/savefile/operator/%3e%3e.md) 
+   [\<\< operator (savefile)](/ref/savefile/operator/%3c%3c.md) 
+   [Export proc (client)](/ref/client/proc/Export.md) 
+   [New proc (client)](/ref/client/proc/New.md) 
+   [procs (savefile)](/ref/savefile/proc.md) 
+   [vars (savefile)](/ref/savefile/var.md) 
+   [tmp vars](/ref/var/tmp.md) 
+   [issaved proc](/ref/proc/issaved.md) 
+   [Read proc (datum)](/ref/datum/proc/Read.md) 
+   [Write proc (datum)](/ref/datum/proc/Write.md) 
::+ {.sidebar .note}


Savefiles are easy to use, but you should always plan what
you\'re going to save and what you don\'t want to save. Use `/tmp` to
avoid saving anything you don\'t need, and you can avoid a lot of
trouble. 

In particular you should be careful that if you\'re
saving a player\'s mob, you don\'t accidentally save any other mobs. If
you save a turf, you should avoid saving its contents unless you know
there are no mobs standing on it (but usually it\'s better to save x,y,z
coordinates than the turf itself). This is explained further in the [tmp
vars](/ref/var/tmp.md)  entry. 

Currently, overlays and underlays also
save by combining each list into a single icon that saves its full icon
data in the file. This may not be desired, so you can remove that data.
Usually you\'ll want to rebuild any overlay/underlay lists during
[Read()](/ref/datum/proc/Read.md) .code}.
:::


A database file in DM is called a \"savefile\". All of the
contents of a savefile reside in a single file. The contents of the file
are stored in database directories. These should not be confused with
real directories in the external file system. The database directories
are all contained inside the one file. 

Each database directory
contains a list of sub-directories and a buffer in which data may be
written. The absolute path to a directory has the following format:
\"/Dir1/Dir2/\...\". The current directory may be set by assigning its
absolute path name to `savefile.cd`. A relative path (one that doesn\'t
begin with \"/\") may also be used, in which case the new path starts at
the current directory. The path \".\" stands for the current directory,
\"..\" for its parent, \"../..\" for its parent\'s parent, etc.


A savefile may be created with `new/savefile(name)`. The
optional name argument may be an external file name (existing or to be
created) in double quotes or a file from the resource cache in single
quotes. Of course, a variable containing either of these types of values
may also be used. If no name is specified, a temporary file will be
created, which will be destroyed when the savefile is no longer in use.
If a resource cache is specified, a temporary file will be created and
the contents of the cached file will be copied into it. Changes will
therefore only be temporary.