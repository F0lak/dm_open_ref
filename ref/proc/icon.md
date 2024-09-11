## icon proc
**See also:**
*   [file proc](/ref/proc/file.md) -m
*   [icon_states proc](/ref/proc/icon_states.md) -m
*   [icons](/ref/DM/icon.md) -m
<!-- -->
**Format:**
*   icon(icon,state,dir,frame,moving)
*   [(supports [named arguments](/ref/proc/arguments/named.md) -m]{.small}
<!-- -->
**Args:**
*   icon* an icon file or /icon object
*   icon_state* an optional text string, specifying a single icon state
    to load
*   dir* an optional direction to extract
*   frame* an optional animation frame to extract
*   moving* Non-zero to extract only movement states, 0 for non-movement
    states, or null (default) for both


This is equivalent to new/icon(). It creates an /icon object,
which is initialized to contain the same graphical data as the given
file. If an icon state or direction are specified, only those parts of
the original icon will be included in the new icon object.