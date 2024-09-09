[]{#/database/query/proc/RowsAffected}    
## RowsAffected proc (database query) {#rowsaffected-proc-database-query byondver="506"}    
**See also:**    
:   [database datum](ref/database)    
:   [database query datum](ref/database/query)    
:   [Execute proc (database query)](ref/database/query/proc/Execute)    
:   [RowsAffected proc (database    
    query)](ref/database/query/proc/RowsAffected)    
<!-- -->    
**Format:**    
:   RowsAffected()    
After running Execute() on a query that changes rows in the database    
(for instance, an UPDATE query), this proc returns the number of rows    
that were changed. This can be useful if you need to know whether a    
query actually did anything.  