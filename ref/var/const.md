## const vars


The const type modifier defines a constant value. This may be
useful for centralizing the location of a value that is used repeatedly
so that it can be easily configured. It has the advantage over #define
macros of obeying the normal scope rules for variables. This means, for
example, that a const variable declared inside a proc will not conflict
with other variables declared elsewhere.
### Example:

```
 mob var/const/max_items = 100 Enter(O) if(src.contents.len
\>= src.max_items) return 0 return ..() 
```
 

This example
defines an upper limit on the number of items a mob may carry.

> [!TIP] 
> **See also:**
> +   [vars](/ref/var.md) 