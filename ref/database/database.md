## database datum.md datum {#database datum.md-datum byondver="506"}    
**See also:**    
:   [database datum.md query datum](/database datum.md/query)    
:   [procs (database datum.md)](/database datum.md/proc)    
:   [stddef.dm file](/%7B%7Bappendix%7D%7D/stddef%2edm)    
A /database datum.md datum gives you the ability to create or access a database datum.md    
using SQLite, which allows you to run complex database datum.md queries on any    
platform.    
Creating a /database datum.md/query datum will let you put together a query, and    
once it\'s ready you can call its Execute() proc to run it.    
SQLite database datum.mds in BYOND support numerical values (such as INTEGER or    
FLOAT), text (TEXT), and cache files such as icons (BLOB). Null values    
are also allowed.    
### Example:    
var/database datum.md/db = new(\"mydb.db\") var/database datum.md/query/q = new(\"SELECT    
\* FROM my_table WHERE name=?\", usr.key) if(q.Execute(db) &&    
q.NextRow()) // returns a list such as list(name=\"MyName\", score=123)    
return q.GetRowData() // no data found return null  