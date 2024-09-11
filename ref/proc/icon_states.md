## icon_states proc
**See also:**
*   [icons](/ref/DM/icon.md) -m
*   [icon_size var (world)](/ref/world/var/icon_size.md) -m
*   [map_format var (world)](/ref/world/var/map_format.md) -m
*   [Big icons](/ref/%7Bnotes%7D/big-icons.md) -m
*   [Tiled icons](/ref/%7Bnotes%7D/tiled-icons.md) -m<!-- -->
**Format:**
*   icon_states(Icon, mode=0)
<!-- -->
**Returns:**
*   A list of text strings.
<!-- -->
**Args:**
*   Icon* the icon being accessed
*   mode* applies to icons larger than one tile when using
    map_format=TILED_ICON_MAP; see below


Icons may have one or more internal states, which are
identified by name. The state \"\" is the default. 

If you are
not using the TILED_ICON_MAP value for world.map_format, you can ignore
the mode argument. 

When graphics bigger than world.icon_size
are used as an icon, and the map_format in use is TILED_ICON_MAP, they
are internally broken up into tiles, one per icon state. The `mode`
argument was added for big icons that get split into several smaller
tiles. Those icons have several smaller states per true icon_state. For
example if your 64×64 icon has a state named \"open\", it will contain
states \"open\", \"open 0,0\", \"open 1,0\", \"open 0,1\", and \"open
1,1\" which are all used internally. (If the state name is blank, the
sub-states are just \"0,0\", etc.) When using the TILED_ICON_MAP format,
you need these for displaying the icon over several different atoms.


mode=0 will only show the sub-states (\"open 0,0\" and so on),
all of which can be safely extracted in a single-tile icon via the
`icon()` proc. mode=1 will show the main state names (\"open\"); any
time you work with that state name you\'re working with the full-size
icon. mode=2 will show all of the states.