## filter proc 
###### BYOND Version 512

<!-- -->
**Format:**
+   filter(type = Type, parameter = Value, \...)


Creates a graphical filter that can be assigned or added to a
list of filters on an atom or image. 

This proc uses named
arguments, and the \"type\" value must always be included. To see which
types of filters are available and what parameters they accept, see
[Filter effects](/ref/%7Bnotes%7D/filters.md) 
### Example:

```
 atom/proc/Highlight(apply) if(apply) filters =
filter(type=\"outline\", size=1, color=rgb(255,0,0)) else filters = null

```
 

A filter created with this proc is an *abstract*
filter; it is not associated with any atom. When you add it to atom\'s
filters, the atom gets a copy of this filter, so changing the abstract
filter\'s values afterward will not change the atom\'s filters. For the
same reason, an abstract filter can\'t be animated. 

A filter
that is part of an atom\'s filters list, like obj.filters\[1\], is an
*attached* filter. Changing the values for an attached filter will
change how that atom is displayed, and attached filters can be animated.
### Named Filters {#named-filters byondver="516"}


Filters can also be given a `name` argument, and can be
referred to in an atom\'s `filters` list via that name (e.g. as
`filters["shadow"]`) instead of a numeric index.

**See also:**
+   [filters var (atom)](/ref/atom/var/filters.md) 
+   [Filter effects](/ref/%7Bnotes%7D/filters.md) 