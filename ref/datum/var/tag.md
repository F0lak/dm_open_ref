## tag var (datum)
**See also:**
*   [locate proc](/ref/proc/locate.md) <!-- -->
**Default value:**
*   null


This may be assigned to a unique text string identifying a
particular object. A reference to the object can then be obtained by
using locate(). 

One reason to use tags is when making
references in the code to objects and locations that will be created on
the map. You can simply edit the object in the map editor, set its tag,
and then use that in the code relating to the object. 

The
following example demonstrates how to set a tag and use it to obtain a
reference to an object.
### Example:

```
 mob/verb/test() var/obj/O = new() O.tag = \"My Object\"
var/obj/O2 = locate(\"My Object\") ASSERT(O == O2) //this should always
be true 
```
 

Setting a tag to \"\" or null removes it.
Any object with a non-empty tag is immune to garbage collection, since
the tag is treated as an implicit reference to that object.