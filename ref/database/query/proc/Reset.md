## Reset proc (database query) 
###### BYOND Version 506
**See also:**
*   [database datum](/ref/database.md) -m
*   [database query datum](/ref/database/query.md) -m
*   [Execute proc (database query)](/ref/database/query/proc/Execute.md) -m
*   [NextRow proc (database query)](/ref/database/query/proc/NextRow.md) -m<!-- -->
**Format:**
*   Reset()


If a query returns any rows of results, Reset() will go back to
the beginning just after Execute() was called. This is useful if you
have called NextRow() repeatedly to retrieve a number of rows, but need
to go back to the start of the query for some other reason. This can
also be used to count the total number of result rows if needed, but for
best performance that isn\'t recommended.