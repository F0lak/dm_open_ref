[]{#/database/proc/Open}    
## Open proc (database) {#open-proc-database byondver="506"}    
**See also:**    
:   [database datum](ref/database)    
:   [Close proc (database)](ref/database/proc/Close)    
:   [New proc (database)](ref/database/proc/New)    
<!-- -->    
**Format:**    
:   Open(filename)    
<!-- -->    
**Args:**    
:   filename: The database filename to open    
Opens a database file. If another database was already open, it is    
closed automatically. It is more common to simply open the database in    
New().  