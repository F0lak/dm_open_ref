## icon_state var (atom)

**Default value:**
+   null


Icons may appear differently depending on the icon state. For
example, turf door icons could have \"open\" and \"closed\" states. If a
state is specified that does not exist in the icon file, the default
null state will be displayed if it exists.
### Example:

``` dm
 turf/door icon_state = \"closed\" density = 1 verb open()
set src in view(1) icon_state = \"open\" density = 0 close() set src in
view(1) icon_state = \"closed\" density = 1 
```


> [!TIP] 
> **See also:**
> +   [flick proc](/ref/proc/flick.md) 
> +   [icon var (atom)](/ref/atom/var/icon.md) 
> +   [icon_states proc](/ref/proc/icon_states.md) <!-- -->