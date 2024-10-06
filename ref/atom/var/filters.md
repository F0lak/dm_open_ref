## filters var (atom) 
###### BYOND Version 512

<!-- -->
**Default value:**
+   empty list


This var is a list of graphical filters to use for
post-processing effects, applied in order. You can assign this value a
list, an individual filter, or null to empty it.
### Example:

```dm
 obj/blurry
 	filters = filter(type="blur", size=1)

```
 

Atoms with the `KEEP_TOGETHER` flag will apply their
filters after the composite image has been drawn. Filters will also
apply to any maptext the atom has. 

See the
[filters](/ref/notes/filters.md) section for more information on
individual filters.
### Named Filters <sub>516</sub>


Filters can be created with a `name` argument. That name can be
used to access the filter in the list (e.g. `filters["drunk_blur"]`
instead of using a numeric index, which is helpful for managing
animations and updating multiple filters on an object. 

Adding a
new filter with the same name as an existing filter will remove the old
one, since only one of a given filter name can be used on an appearance
at a time. 

You can also remove a named filter from the list
simply by subtracting the name instead of the filter itself. That is,
`filters -= filters["foo"]` and `filters -= "foo"` do the same thing.

> [!TIP] 
> **See also:**
> +   [appearance_flags var (atom)](/ref/atom/var/appearance_flags.md) 
> +   [filter proc](/ref/proc/filter.md) 
> +   [animate proc](/ref/proc/animate.md) 
> +   [Filter effects](/ref/notes/filters.md) 