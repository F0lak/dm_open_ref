[]{#/NextRow proc (database query).md}    
## NextRow proc (database query) {#nextrow-proc-database-query byondver="506"}    
**See also:**    
:   [database datum](/database)    
:   [database query datum](/database/query)    
:   [Execute proc (database query)](/database/query/proc/Execute)    
:   [GetColumn proc (database query)](/database/query/proc/GetColumn)    
:   [GetRowData proc (database query)](/database/query/proc/GetRowData)    
:   [Reset proc (database query)](/database/query/proc/Reset)    
<!-- -->    
**Format:**    
:   NextRow()    
If there are result rows in this query (Execute() must be called to run    
the query first), NextRow() will retrieve the next row and return 1 if    
it found a row, or 0 if the results are all finished. NextRow() is    
typically called in a while() loop.    
After calling NextRow(), you can call GetColumn() or GetRowData() to get    
information about the results in this row.    
Call Reset() if you want to rewind the query to the beginning.  