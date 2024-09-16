## datum

The datum object is the ancestor of all other data types in DM,
with only a few exception called primitives. That means that the
variables and procedures of /datum are inherited by almost all other
types of objects. 

When you define a new "top level" object,
if you do not specify a parent_type, it defaults to /datum.
### Example:

``` dm
datum
  //definitions to be shared by all object types
  proc/DebugMe()
    world.log << "/datum properties:"
    world.log << "type: [type]"
    world.log << "parent_type: [parent_type]"
    return ..()
    
MyType
  var myvar = "test
  DebugMe()
    world.log << "/MyType properties:"
    world.log << "myvar: [myvar]"
    return ..() //this calls /datum/proc/DebugMe() 
```

### Primitives <sub><sub>516</sub></sub>
Primitive types do not descend from /datum. These have no
subtypes, and may or may not be able to allow var and proc overrides.

  | Type | User-defined | Can Override | Notes |
  | ----- | ----- | ----- | ----- |
  | [/world](/ref/world.md) | procs only | vars and procs |                           
  [/client](/ref/client.md) | vars and procs | vars and procs |  can manually set `parent_type=/datum`  <br>can\'t be created in [new](/ref/proc/new.md) 
  [/list](/ref/list.md) | \- | \- | | 
  [/savefile](/ref/savefile.md) | \- |  [byond_version](/ref/savefile/var/byond_version.md)<br> [byond_build](/ref/savefile/var/byond_build.md)         
  [/alist](/ref/alist.md) | \- | \- | |
  [/pixloc](/ref/pixloc.md) | \- | \- | |
  [/vector](/ref/vector.md) | \- |\- | |
  [/callee](/ref/pixloc.md) | \- |\- | can\'t be created in [new](/ref/proc/new.md)|


> [!TIP] 
> **See also:**
> +   [atom](/ref/atom.md) 
> +   [procs (datum)](/ref/datum/proc.md) 
> +   [vars (datum)](/ref/datum/var.md) 