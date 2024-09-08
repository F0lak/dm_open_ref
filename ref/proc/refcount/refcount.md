[]{#/proc/refcount}
## refcount proc {#refcount-proc byondver="515"}
**See also:**
:   [garbage collection](#/DM/garbage)
<!-- -->
**Format:**
:   refcount(Object)
<!-- -->
**Args:**
:   Object: The object to get a reference count for
<!-- -->
**Returns:**
:   A count of references for the object.
This gets a reference count for a value, not including the reference
that was placed on the stack while evaluating this proc.
A return value of 0 can mean one of several things: Either this was the
last reference and the object was subsequently deleted after refcount(),
or the value doesn\'t support reference counting.
Note: A nonzero return value does not necessarily mean the object will
be deleted when its count reaches zero; mobs for instance will not be
soft-deleted by the garbage collector if their `key` var is set, and
some objects like clients and areas never soft-delete. A zero value also
does not necessarily mean the object is immortal; it may be transient,
like the `args` list in a proc that only lives as long as that copy of
the proc lives.