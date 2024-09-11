## datum
**See also:**
*   [atom](/atom)
*   [procs (datum)](/datum/proc)
*   [vars (datum)](/datum/var)


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
  [`/world`](/world)         procs only        vars and procs                                          
  [`/client`](/client)       vars and procs    vars and procs                                          can manually set
                                                                                                             `parent_type=/datum`\
                                                                                                             can\'t be created in
                                                                                                             [`new`](/proc/new)
  [`/list`](/list)           \-                \-                                                      
  [`/savefile`](/savefile)   \-                [`byond_version`](/savefile/var/byond_version)\   
                                                     [`byond_build`](/savefile/var/byond_build)        
  [`/alist`](/alist)         \-                \-                                                      
  [`/pixloc`](/pixloc)       \-                \-                                                      
  [`/vector`](/vector)       \-                \-                                                      
  [`/callee`](/pixloc)       \-                \-                                                      can\'t be created in
                                                                                                             [`new`](/proc/new)
  -------------------------------------------------------------------------------------------------------------------------------------