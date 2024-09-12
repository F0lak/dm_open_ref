## in operator
**See also:**
+   [list](/ref/list.md) 
+   [operators](/ref/operator.md) 
+   [! operator](/ref/operator/!.md) 
+   [locate proc](/ref/proc/locate.md) 
+   [input proc](/ref/proc/input.md) 
<!-- -->
**Format:**
+   A in List
**Returns:**
**1 if A exists in List; 0 if not**


This is a relatively safe way to check if an item is in a list,
because the value of `List` is allowed to be a non-list value, such as
null. Compare to `List.Find(A)` which will fail if `List` is not an
actual list. 

`List` can also be an atom, in which case
`A in List` is equivalent to `A in List.contents`.
::+ note


The `in` operator has a lower precedence than `!`, which can be
a point of confusion. If you want to check if something is *not* in a
list, it\'s a common mistake to try `if(!A in List)`. Unfortunately the
`!A` part is evaluated first and becomes 0 or 1, so you\'re really
asking if 0 or 1 is in the list. The correct way to check if something
is not in a list is to wrap the `in` operator and its operands with
parentheses, as in `if(!(A in List))`. 

Similarly, the
assignment operators also have higher precedence than `in`, so
`has_thing = thing in src` will not be interpreted as you might expect.
Again the solution is to use parentheses, e.g.
`has_thing = (thing in src)`.
:::


The `in` operator is also a modifier for some procs such as
[locate()](/ref/proc/locate.md) {.code} and [input()](/ref/proc/input.md) {.code}.
Note+ For [associative lists](/ref/list/associations.md) there\'s a faster way
to see if an item is in that list. The lookup of `List[A]` in an
associative list is relatively fast, so if the associated value is
always expected to be true (not null, 0, or an empty string), you can
use `List[A]` instead of `A in List` in those situations.