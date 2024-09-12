## flist proc
**See also:**
*   [fexists proc](/ref/proc/fexists.md) <!-- -->
**Format:**
*   flist(Path)
<!-- -->
**Args:**
*   Path* The path in the filesystem to get a listing of.
<!-- -->
**Returns:**
*   A list of files contained in the specified directory and whose names
    begin with the specified text. The names of sub-directories are
    listed too, and are marked by a trailing \"/\".


The path is of the form \"dir1/dir2/\.../file\". Only files
beginning with the \"file\" part are listed, so be sure to end a
directory name with \"/\" if you wish to see its contents. Otherwise you
will just get that directory name back with a \"/\" appended.


Only files and sub-directories directly contained in the
specified path are listed (ie not the contents of the sub-directories
too). The file names in the list do not include the path information but
just the bare file name.