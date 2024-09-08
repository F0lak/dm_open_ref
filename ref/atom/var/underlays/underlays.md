[]{#/atom/var/underlays}
## underlays var (atom)
**See also:**
:   [icon var (atom)](#/atom/var/icon)
:   [list](#/list)
:   [overlays var (atom)](#/atom/var/overlays)
:   [Understanding the renderer](#/%7Bnotes%7D/renderer)
<!-- -->
**Default value:**
:   empty list
This is a list of icons which are displayed underneath the object\'s
main icon. Since these are basically the same as overlays, see
[overlays](#/atom/var/overlays) for more detailed information.
The only real differences between items in the underlays list vs. the
overlays list is that they\'re processed first, and if they use
`FLOAT_LAYER` (or any other negative layer value) they\'ll appear below
the object instead of above it. For this reason, the underlays list
isn\'t used nearly as much as overlays since it\'s easier to throw most
things into the overlays list.
When multiple turfs are stacked on top of one another in the map editor,
there is actually only one turf (the topmost) and the rest are all
underlays.