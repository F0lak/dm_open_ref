## typesof proc
**See also:**
*   [istype proc](/ref/proc/istype.md) -m
*   [locate proc](/ref/proc/locate.md) -m<!-- -->
**Format:**
*   typesof(Type1,Type2,\...)
<!-- -->
**Returns:**
*   A list of all types that are derived from the specified \"base\"
    types, including the base types themselves.
<!-- -->
**Args:**
*   The \"base\" types.
### Example:

```
 obj/fruit apple peach mango var/list/fruit_types =
typesof(/obj/fruit) 
```
 

In this example, fruit_types is
initialized to contain /obj/fruit, /obj/fruit/apple, /obj/fruit/peach,
and /obj/fruit/mango. 

This procedure can also be used to list
procs and verbs.
### Example:

```
 mob/admin_commands/verb shutdown_world() world.Del()
reboot_world() world.Reboot() //for testing mob/verb/add_admin() verbs
+= typesof(/mob/admin_commands/verb) mob/verb/remove_admin() verbs -=
typesof(/mob/admin_commands/verb) 
```
