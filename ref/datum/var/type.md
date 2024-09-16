# type var (datum)
**Default value:**
+   The "type path" of the object definition.

All objects in BYOND are a part of the object tree.  the `type` variable is the path of the objects definition on the object tree, similar to a file path on your computer.
```dm
mob
	player
		// type is /mob/player
	enemy
		// type is /mob/enemy

obj
	item
		sword
			// type is /obj/item/sword
	trap
		// type is /obj/trap
```

> [!IMPORTANT]
> This variable is read-only. 
>
> ``` dm
> mob/verb/test()
> usr << type //displays "/mob" 
> ```
