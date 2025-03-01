## global/static vars


The global type modifier makes a var permanent and shared. This
means only one copy of the var is maintained. Otherwise, separate copies
of the var are maintained for each instance containing the var (be it a
proc, mob, obj, etc.) The 'static' keyword can also be used, they both do the same thing.
### Example:

```dm
 mob/proc/Counter() var/global/count src << "Count =
[++count]" 
```
 

This example increases the count each
time the proc is called. If count were not declared global, the
displayed count would be 1 every time.

> [!TIP]
> **See also:**
> +   [vars](/ref/var.md)
> +   [Forum discussion](https://web.archive.org/web/20250301052813/https://www.byond.com/forum/post/137782#comment936991)
