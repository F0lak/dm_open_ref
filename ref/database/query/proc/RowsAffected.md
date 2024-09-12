## RowsAffected proc (database query) 
###### BYOND Version 506
**See also:**
+   [database datum](/ref/database.md) 
+   [database query datum](/ref/database/query.md) 
+   [Execute proc (database query)](/ref/database/query/proc/Execute.md) 
+   [RowsAffected proc (database
    query)](/ref/database/query/proc/RowsAffected.md) <!-- -->
**Format:**
+   RowsAffected()


After running Execute() on a query that changes rows in the
database (for instance, an UPDATE query), this proc returns the number
of rows that were changed. This can be useful if you need to know
whether a query actually did anything.