## Columns proc (database query) 
###### BYOND Version 506
**See also:**
*   [database query datum](/database/query)
*   [Execute proc (database query)](/database/query/proc/Execute)
*   [GetColumn proc (database query)](/database/query/proc/GetColumn)
*   [GetRowData proc (database query)](/database/query/proc/GetRowData)
*   [NextRow proc (database query)](/database/query/proc/NextRow)
<!-- -->
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