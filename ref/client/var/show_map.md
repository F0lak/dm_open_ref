## show_map var (client)

**Default value:**
+   1


This variable may be used to turn off the view of the map in
Dream Seeker. This could be useful for making text MUDs where the rooms
are turfs (ie most rooms can be laid out on a grid but you don\'t want
the user interface to show the map in any way). 

The following
example shows one useful combination of settings. Note that setting
`world.view=-1` also disables the map, but it also sets the default
value of the `view()` depth in such a way as to always return an empty
list.
### Example:

```
 client show_map = 0 //Text is best! world view = 0 //You can
interact only with objects in same turf. mob density = 0 //Allow
multiple mobs in a room. 
```


> [!TIP] 
> **See also:**
> +   [show_verb_panel var (client)](/ref/client/var/show_verb_panel.md) 
> +   [view var (client)](/ref/client/var/view.md) 
> +   [view var (world)](/ref/world/var/view.md) <!-- -->