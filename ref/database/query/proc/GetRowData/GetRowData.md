[]{#/database/query/proc/GetRowData}    
## GetRowData proc (database query) {#getrowdata-proc-database-query byondver="506"}    
**See also:**    
:   [database datum](/ref/database/database.md)    
:   [database query datum](/ref/database/query/query.md)    
:   [Columns proc (database query)](/ref/database/query/proc/Columns/Columns.md)    
:   [Execute proc (database query)](/ref/database/query/proc/Execute/Execute.md)    
:   [GetColumn proc (database query)](/ref/database/query/proc/GetColumn/GetColumn.md)    
:   [NextRow proc (database query)](/ref/database/query/proc/NextRow/NextRow.md)    
:   [Reset proc (database query)](/ref/database/query/proc/Reset/Reset.md)    
<!-- -->    
**Format:**    
:   GetRowData()    
Returns a list with the current result row for this query. If you    
haven\'t already called Execute() and NextRow(), you should do that    
first.    
The list returned is an associative list with name=value pairs. A    
typical result might look like this:    
`list("name" = "Tom", "quest" = "Save a Dog", complete = 1)`    
The values returned depend on what type the database table thinks they    
are. For instance if you defined a column as INTEGER or FLOAT, the value    
should be a number. TEXT is still text, and null values are returned as    
null. If an icon was saved into a BLOB field, the result is an icon    
file.  