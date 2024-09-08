[]{#/database/proc/Close}
## Close proc (database) {#close-proc-database byondver="506"}
**See also:**
:   [database datum](#/database)
:   [Open proc (database)](#/database/proc/Open)
<!-- -->
**Format:**
:   Close()
If a database is currently open, this will close the database and any
queries currently running in it. Usually you don\'t need to call this
directly, because deleting the datum will do it for you.