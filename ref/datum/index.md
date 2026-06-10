
## datum (info)
***
The datum object is the ancestor of all other data types in DM, with only a few exception called primitives. That means that the variables and procedures of /datum are inherited by almost all other types of objects.

When you define a new "top level" object, if you do not specify a parent_type, it defaults to /datum.


```dm

datum
   //definitions to be shared by all object types
   proc/DebugMe()
      world.log << "/datum properties:"
      world.log << "type: [type]"
      world.log << "parent_type: [parent_type]"
      return ..()

MyType
   var
      myvar = "test"
   DebugMe()
      world.log << "/MyType properties:"
      world.log << "myvar: [myvar]"
      return ..() //this calls /datum/proc/DebugMe()

```


Primitive types do not descend from /datum. These have no subtypes, and may or may not be able to allow var and proc overrides.
***
**Related Pages:**
+    [atom](/ref/atom)
+    [procs (datum)](/ref/datum/proc)
+    [vars (datum)](/ref/datum/var)
