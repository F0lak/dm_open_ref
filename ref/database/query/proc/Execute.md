## Execute proc (database query) 
###### BYOND Version 506
**See also:**
*   [database datum](/ref/database.md) 
*   [database query datum](/ref/database/query.md) 
*   [Add proc (database query)](/ref/database/query/proc/Add.md) 
*   [Close proc (database query)](/ref/database/query/proc/Close.md) 
*   [GetColumn proc (database query)](/ref/database/query/proc/GetColumn.md) 
*   [GetRowData proc (database query)](/ref/database/query/proc/GetRowData.md) 
*   [NextRow proc (database query)](/ref/database/query/proc/NextRow.md) 
*   [Reset proc (database query)](/ref/database/query/proc/Reset.md) 
*   [RowsAffected proc (database
    query)](/ref/database/query/proc/RowsAffected.md) <!-- -->
**Format:**
*   Execute(database)
<!-- -->
**Args:**
*   database* A /database datum with the database to be queried, or the
    name of the database file


Runs a database query. Once the query is run, if the query is
supposed to returns any rows you can call NextRow() until finished, and
then GetColumn() or GetRowData() to get the information from each row.
For queries that cause changes, RowsAffected() is also a useful call.


The database argument is optional after the first time you use
it. 

You can use a filename instead of a /database datum, as a
shortcut; the datum will be created for you. 

After a query is
executed, calling Add() to create new query text will clear out the old
query text automatically.
### Example:

```
 var/database/db = new(\"mydb.db\") var/database/query/q =
new(\"SELECT quest,complete FROM quests WHERE name=?\", usr.key)
if(!q.Execute(db)) return null var/list/completed_quests = new
while(q.NextRow()) var/row = q.GetRowData() if(row\[\"complete\"\])
completed_quests\[row\[\"quest\"\]\] = 1 return completed_quests

```
