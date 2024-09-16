## New proc (database query) 
###### BYOND Version 506

<!-- -->
**Format:**
+   New(text, item1, item2, ...)
<!-- -->
**Args:**
+   text: Text to add to the query
+   item1, item2, etc.: Items that will replace question marks in text


Creates a new query and adds text by automatically calling
Add(). See the [Add proc](/ref/database/query/proc/Add.md) for more
information. 

Call Execute() to run the query.

> [!TIP] 
> **See also:**
> +   [database datum](/ref/database.md) 
> +   [database query datum](/ref/database/query.md) 
> +   [Add proc (database query)](/ref/database/query/proc/Add.md) 