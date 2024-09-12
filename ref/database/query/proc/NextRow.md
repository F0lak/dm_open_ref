## NextRow proc (database query) 
###### BYOND Version 506

**Format:**
+   NextRow()


If there are result rows in this query (Execute() must be
called to run the query first), NextRow() will retrieve the next row and
return 1 if it found a row, or 0 if the results are all finished.
NextRow() is typically called in a while() loop. 

After calling
NextRow(), you can call GetColumn() or GetRowData() to get information
about the results in this row. 

Call Reset() if you want to
rewind the query to the beginning.

**See also:**
+   [database datum](/ref/database.md) 
+   [database query datum](/ref/database/query.md) 
+   [Execute proc (database query)](/ref/database/query/proc/Execute.md) 
+   [GetColumn proc (database query)](/ref/database/query/proc/GetColumn.md) 
+   [GetRowData proc (database query)](/ref/database/query/proc/GetRowData.md) 
+   [Reset proc (database query)](/ref/database/query/proc/Reset.md) <!-- -->