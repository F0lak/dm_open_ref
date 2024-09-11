## ftime proc
**See also:**
*   [time2text proc](/ref/proc/time2text.md) -m
*   [flist proc](/ref/proc/flist.md) -m
*   [fexists proc](/ref/proc/fexists.md) -m
*   [length proc](/ref/proc/length.md) -m<!-- -->
**Format:**
*   ftime(File, IsCreationTime)
<!-- -->
**Args:**
*   File* name of file to test
*   IsCreationTime (optional)* true to return file creation time, false
    (default) to return last-modified time
<!-- -->
**Returns:**
*   A time value that can be sent to time2text().