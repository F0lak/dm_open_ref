## GetColumn proc (database query) 
###### BYOND Version 506
**See also:**
+   [database datum](/ref/database.md) 
+   [database query datum](/ref/database/query.md) 
+   [Columns proc (database query)](/ref/database/query/proc/Columns.md) 
+   [Execute proc (database query)](/ref/database/query/proc/Execute.md) 
+   [GetRowData proc (database query)](/ref/database/query/proc/GetRowData.md) 
+   [NextRow proc (database query)](/ref/database/query/proc/NextRow.md) 
+   [Reset proc (database query)](/ref/database/query/proc/Reset.md) <!-- -->
**Format:**
+   GetColumn(column)
<!-- -->
**Args:**
+   column: The column number whose value should be retrieved


Gets the value from the Nth column in this row of results. If
you haven\'t already called Execute() and NextRow(), you should do that
first. 

To get the name of the column, not the value for this
row, call Columns(column) instead. 

The value returned depends
on what type the database table thinks it is. For instance if you
defined a column as INTEGER or FLOAT, the value should be a number. TEXT
is still text, and null values are returned as null. If an icon was
saved into a BLOB field, the result is an icon file.