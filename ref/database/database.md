## database datum 
###### BYOND Version 506

A /database datum gives you the ability to create or access a
database using SQLite, which allows you to run complex database queries
on any platform. 

Creating a /database/query datum will let you
put together a query, and once it\'s ready you can call its Execute()
proc to run it. 

SQLite databases in BYOND support numerical
values (such as INTEGER or FLOAT), text (TEXT), and cache files such as
icons (BLOB). Null values are also allowed.
### Example:

```dm
var/database/db = new("mydb.db")
var/database/query/q = new("SELECT * FROM my_table WHERE name=?", usr.key)

if(q.Execute(db) && q.NextRow())
    // returns a list such as list(name="MyName", score=123)
    return q.GetRowData()
// no data found
return null
```

> [!TIP] 
> **See also:**
> +   [database query datum](/ref/database/query.md) 
> +   [procs (database)](/ref/database/proc.md) 
> +   [stddef.dm file](/ref/appendix/stddef%2edm.md) 