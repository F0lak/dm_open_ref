## NextRow proc (database query) 
###### BYOND Version 506
**See also:**
*   [database datum](/ref/database.md) -m
*   [database query datum](/ref/database/query.md) -m
*   [Execute proc (database query)](/ref/database/query/proc/Execute.md) -m
*   [GetColumn proc (database query)](/ref/database/query/proc/GetColumn.md) -m
*   [GetRowData proc (database query)](/ref/database/query/proc/GetRowData.md) -m
*   [Reset proc (database query)](/ref/database/query/proc/Reset.md) -m<!-- -->
**Format:**
*   NextRow()


If there are result rows in this query (Execute() must be
called to run the query first), NextRow() will retrieve the next row and
return 1 if it found a row, or 0 if the results are all finished.
NextRow() is typically called in a while() loop. 

After calling
NextRow(), you can call GetColumn() or GetRowData() to get information
about the results in this row. 

Call Reset() if you want to
rewind the query to the beginning.