## arguments (proc)

The parameters to a proc are referred to as arguments. To
define argument variables, place them inside the ()\'s in the proc
definition. A default value may be specified. Otherwise, arguments
default to null.
### Example:

``` dm
proc/Sum(a,b)
  return a + b
```

### Example:

``` dm
proc/set_mob_desc(mob/M,desc="big and bad")
  M.desc = desc
  world << "The new desc for [M] is [desc]."
```

Note how the variable type may be specified. It is just like
any other variable definition, except "`var/`" is implicit and does
not need to be typed.

> [!TIP] 
> **See also:**
> +   [named arguments (proc)](/ref/proc/arguments/named.md) 
> +   [path operators](/ref/operator/path.md) 
> +   [arglist proc](/ref/proc/arglist.md) 
> +   [args var (proc)](/ref/proc/var/args.md) 