## Add proc (database query) 
###### BYOND Version 506
**See also:**
+   [database query datum](/ref/database/query.md) 
+   [Clear proc (database query)](/ref/database/query/proc/Clear.md) <!-- -->
**Format:**
+   Add(text, item1, item2, \...)
<!-- -->
**Args:**
+   text: Text to add to the query
+   item1, item2, etc.: Items that will replace question marks in text


Adds text to a database query. If this datum was already used
to run a query, Clear() will be called automatically. 

If your
text includes question marks, they will be replaced with the other items
listed in the proc arguments. If that item is a string, quotes will be
put around it for the query text. Files in the cache (such as icons)
will be added as BLOB values. 

After the query has been built,
call Execute() to run it.
### Example:

```
 var/database/db = new(\"mydb.db\") var/database/query/q = new
q.Add(\"INSERT INTO quests (name, quest, complete) VALUES (?,?,?)\",
usr.key, quest_name, 1) q.Execute(db) 
```
 

In the example
above, the query text might look like this:


`INSERT INTO quests (name, quest, complete) VALUES ('Tom','Save the Dog',1)`