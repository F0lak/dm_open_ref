## garbage collection
**See also:**
*   [del proc](/ref/proc/del.md) -m
*   [world](/ref/world.md) -m
*   [refcount proc](/ref/proc/refcount.md) -m


At runtime, data objects are garbage collected. That means data
which is no longer in use gets automatically deleted to free up system
memory. This applies to text strings, lists, savefiles, datum objects,
and so on. 

The garbage collector works by using an efficient
reference counting system. Once an item is no longer referenced by any
variable, it gets deleted. For the most part, that frees you from having
to think about memory allocation, which is wonderful, especially in the
case of text strings, which tend to be allocated on the fly all over the
place. 

There are a couple provisos that you should note. One is
that circular references will never be deleted by the garbage collector.
By *circular reference*, I mean a pair of objects with variables that
point to each other, or even an object with a variable that points to
itself. In rare cases, you may even depend on this behavior. When you
are done with such objects, you should either null out the circular
reference, or you should forcibly destroy each object with the `del`
instruction.
::* {.sidebar .underhood}


This is a quick list of things that count as references to an
object:
-   Stored in a var
-   An item in a [list](/ref/list.md) -m, or [associated](/ref/list/associations.md) -m
    with a list item
-   Has a [tag](/ref/datum/var/tag.md) -m{.code}
-   Is on the map (always true for [turfs](/ref/turf.md) -m)
-   Inside another atom\'s [contents](/ref/atom/var/contents.md) -m{.code}
-   Inside an atom\'s [vis_contents](/ref/atom/var/vis_contents.md) -m{.code}
-   A temporary value in a still-running proc
-   Is a [mob](/ref/mob.md) -m with a [key](/ref/mob/var/key.md) -m{.code}
-   Is an [image object](/ref/image.md) -mattached to an atom


`del()` will try to clear out the most obvious possible
references first, and bail out when it\'s done, but if there are still
references it will search everywhere for any references that remain.
:::


An object with running or sleeping procs is referenced by the
`src` variable of those procs and will therefore not be thrown out.


Another note is that the `world.contents` list does not count
as a reference. Otherwise, `/mob` and `/obj` objects would never be
deleted, which is not the case. Note that objects which are contained by
another object or which contain objects themselves *are* referenced and
will not be deleted. That means an object must be at `loc=null` with no
contents and, of course, no other references anywhere in order to get
deleted by the garbage collector. 

Mobs with a non-empty `key`
and all objects with non-empty `tag` are also immortal. 

Turfs
and areas do not currently get garbage collected. 

When the
world shuts down, all objects are destroyed, whether they are referenced
or not. You don\'t have to worry about system memory getting consumed by
persistent objects. That doesn\'t happen. 

In general, people
who do not like reference counting garbage collection should be happy
that DM provides a `del` instruction, allowing you to take charge and
delete things whether they are referenced or not. Another nicety is that
this automatically nulls out any existing references to the object, so
you don\'t end up with dangling references to a deleted object, which
can otherwise be a great source of instability and mysterious bugs.