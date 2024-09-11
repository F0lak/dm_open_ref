## RowsAffected proc (database query) 
###### BYOND Version 506
**See also:**
*   [database datum](/ref/database.md) -m
*   [database query datum](/ref/database/query.md) -m
*   [Execute proc (database query)](/ref/database/query/proc/Execute.md) -m
*   [RowsAffected proc (database
    query)](/ref/database/query/proc/RowsAffected.md) -m<!-- -->
**Format:**
*   RowsAffected()


After running Execute() on a query that changes rows in the
database (for instance, an UPDATE query), this proc returns the number
of rows that were changed. This can be useful if you need to know
whether a query actually did anything.