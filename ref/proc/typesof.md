
## typesof (proc)

**Format:**
+   typesof(Type1,Type2,...)

**Arguments:**
+   The "base" types.

**Returns:**
+   A list of all types that are derived from the specified "base" types,
including the base types themselves.
***

```dm

obj/fruit
  apple
  peach
  mango
var/list/fruit_types = typesof(/obj/fruit)

```


In this example, fruit_types is initialized to contain /obj/fruit, /obj/fruit/apple, /obj/fruit/peach, and /obj/fruit/mango.

This procedure can also be used to list procs and verbs.


```dm

mob/admin_commands/verb
   shutdown_world()
      world.Del()
   reboot_world()
      world.Reboot()

//for testing
mob/verb/add_admin()
   verbs += typesof(/mob/admin_commands/verb)
mob/verb/remove_admin()
   verbs -= typesof(/mob/admin_commands/verb)

```

***
**Related Pages:**
+    [istype proc](/ref/proc/istype)
+    [locate proc](/ref/proc/locate)
