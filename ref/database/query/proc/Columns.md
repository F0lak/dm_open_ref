## Columns proc (database query) 
###### BYOND Version 506
**See also:**
*   [database query datum](/ref/database/query.md) -m
*   [Execute proc (database query)](/ref/database/query/proc/Execute.md) -m
*   [GetColumn proc (database query)](/ref/database/query/proc/GetColumn.md) -m
*   [GetRowData proc (database query)](/ref/database/query/proc/GetRowData.md) -m
*   [NextRow proc (database query)](/ref/database/query/proc/NextRow.md) -m<!-- -->
**Format:**
*   Columns()\
    *or*\
    Columns(column)
<!-- -->
**Args:**
*   column* The Nth column whose name should be read


Returns a list of column names for the current query, or the
name of the Nth column. 

You must call Execute() before calling
Columns().