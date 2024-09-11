## datum
**See also:**
*   [atom](/ref/atom.md) -m
*   [procs (datum)](/ref/datum/proc.md) -m
*   [vars (datum)](/ref/datum/var.md) -m


The datum object is the ancestor of all other data types in DM,
with only a few exception called primitives. That means that the
variables and procedures of /datum are inherited by almost all other
types of objects. 

When you define a new \"top level\" object,
if you do not specify a parent_type, it defaults to /datum.
### Example:

```
 datum //definitions to be shared by all object types
proc/DebugMe() world.log \<\< \"/datum properties:\" world.log \<\<
\"type* \[type\]\" world.log \<\< \"parent_type* \[parent_type\]\"
return ..() MyType var myvar = \"test\" DebugMe() world.log \<\<
\"/MyType properties:\" world.log \<\< \"myvar* \[myvar\]\" return ..()
//this calls /datum/proc/DebugMe() 
```

### Primitives


Primitive types do not descend from /datum. These have no
subtypes, and may or may not be able to allow var and proc overrides.
  -------------------------------------------------------------------------------------------------------------------------------------
  Type                             User-defined      Can override                                            Notes
  -------------------------------- ----------------- ------------------------------------------------------- --------------------------
  [/world](/ref/world.md) -m{.code}         procs only        vars and procs                                          
  [/client](/ref/client.md) -m{.code}       vars and procs    vars and procs                                          can manually set
                                                                                                             `parent_type=/datum`\
                                                                                                             can\'t be created in
                                                                                                             [new](/ref/proc/new.md) -m{.code}
  [/list](/ref/list.md) -m{.code}           \-                \-                                                      
  [/savefile](/ref/savefile.md) -m{.code}   \-                [byond_version](/ref/savefile/var/byond_version.md) -m{.code}\   
                                                     [byond_build](/ref/savefile/var/byond_build.md) -m{.code}        
  [/alist](/ref/alist.md) -m{.code}         \-                \-                                                      
  [/pixloc](/ref/pixloc.md) -m{.code}       \-                \-                                                      
  [/vector](/ref/vector.md) -m{.code}       \-                \-                                                      
  [/callee](/ref/pixloc.md) -m{.code}       \-                \-                                                      can\'t be created in
                                                                                                             [new](/ref/proc/new.md) -m.code}
  -------------------------------------------------------------------------------------------------------------------------------------