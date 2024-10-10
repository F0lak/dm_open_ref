## area

Areas are derived from `/area`, which derives from `/atom`.
Regions on the map may be assigned to an area by painting it onto the
map.  All turfs must have an area, and it defaults to [`world.area`](ref/world/var/area.md)
unless otherwise specified.

For each area type defined in code, one area object is created at
runtime. By default, for all areas on the map, all squares with the same area type
belong to the same instance of the area. However, new variants added in the map editor
with unique variables (ie: `color = "red"`, `tag = "darkness"`) are considered unique 
instances of the same type.

The following example defines the area prototype `/area/outside`. It also
defines an action to be taken when somebody enters an area, namely to
display its description.
### Example:

```dm
area
	Entered(O)
		if(desc)
			O << desc
			return ..()
outside
	desc = "Ah! A breath of fresh air!" 
```

## Rooms
Areas off the map serve as rooms that objects may enter and exit.
Additional instances of rooms may be created from the same type by explicitly creating them
with null as the initial location. That is, the first argument to
`new()` should either be `null` or left unspecified. 

> [!TIP] 
> **See also:**
> +   [atom](/ref/atom.md) 
> +   [procs (area)](/ref/area/proc.md) 
> +   [rooms](/ref/area/room.md) 
> +   [vars (area)](/ref/area/var.md) 
