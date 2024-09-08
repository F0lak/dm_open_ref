[]{#/atom/var/icon_state}
## icon_state var (atom)
**See also:**
:   [flick proc](#/proc/flick)
:   [icon var (atom)](#/atom/var/icon)
:   [icon_states proc](#/proc/icon_states)
<!-- -->
**Default value:**
:   null
Icons may appear differently depending on the icon state. For example,
turf door icons could have \"open\" and \"closed\" states. If a state is
specified that does not exist in the icon file, the default null state
will be displayed if it exists.
### Example:
turf/door icon_state = \"closed\" density = 1 verb open() set src in
view(1) icon_state = \"open\" density = 0 close() set src in view(1)
icon_state = \"closed\" density = 1