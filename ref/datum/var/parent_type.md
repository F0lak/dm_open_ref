## parent_type var
**Default value:**
+   The path of the object definition that contains this one.


This variable is set at compile-time to specify the inheritance
of an object type. Normally, a new type of object inherits its variables
and procedures from the object type that contains it. For example:

```
 obj var weight color sword //parent type of \'sword\'
defaults to /obj weight = 30 color = \"black\" 
```



Explicitly setting the parent type allows you to put the object
definition any place you want. That often means putting it at the top
\"root\" level. Example: 
```
 Armor parent_type = /obj var
strength plate //parent type is /Armor, which in turn inherits from /obj
weight = 100 color = \"rusty\" strength = 10 
```
 

If you
don\'t specify the parent_type for an object defined at the top level,
it defaults to [/datum](/ref/datum.md)  which (with just a couple exceptions)
is the ultimate ancestor of all object types. You could use that fact to
define procedures or variables that you need all of your objects to
share.
### Example:

```
 datum proc/Copy(datum/O) MyType var foo Copy(MyType/O) foo =
O.foo return ..() 
```


> [!TIP] 
> 