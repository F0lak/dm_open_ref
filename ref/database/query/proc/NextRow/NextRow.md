[]{#/database/query/proc/NextRow}    
## NextRow proc (database query) {#nextrow-proc-database-query byondver="506"}    
**See also:**    
:   [database datum](/ref/database/database.md)    
:   [database query datum](/ref/database/query/query.md)    
:   [Execute proc (database query)](/ref/database/query/proc/Execute/Execute.md)    
:   [GetColumn proc (database query)](/ref/database/query/proc/GetColumn/GetColumn.md)    
:   [GetRowData proc (database query)](/ref/database/query/proc/GetRowData/GetRowData.md)    
:   [Reset proc (database query)](/ref/database/query/proc/Reset/Reset.md)    
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