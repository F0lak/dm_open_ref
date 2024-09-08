[]{#/proc/ftime}
## ftime proc
**See also:**
:   [time2text proc](#/proc/time2text)
:   [flist proc](#/proc/flist)
:   [fexists proc](#/proc/fexists)
:   [length proc](#/proc/length)
<!-- -->
**Format:**
:   ftime(File, IsCreationTime)
<!-- -->
**Args:**
:   File: name of file to test
:   IsCreationTime (optional): true to return file creation time, false
    (default) to return last-modified time
<!-- -->
**Returns:**
:   A time value that can be sent to time2text().