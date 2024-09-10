[]{#/icon proc.md}    
## icon proc    
**See also:**    
:   [file proc](/proc/file)    
:   [icon_states proc](/icon proc.md_states)    
:   [icons](/DM/icon)    
<!-- -->    
**Format:**    
:   icon(icon,state,dir,frame,moving)    
:   [(supports [named arguments](/proc/arguments/named))]{.small}    
<!-- -->    
**Args:**    
:   icon: an icon file or /icon object    
:   icon_state: an optional text string, specifying a single icon state    
    to load    
:   dir: an optional direction to extract    
:   frame: an optional animation frame to extract    
:   moving: Non-zero to extract only movement states, 0 for non-movement    
    states, or null (default) for both    
This is equivalent to new/icon(). It creates an /icon object, which is    
initialized to contain the same graphical data as the given file. If an    
icon state or direction are specified, only those parts of the original    
icon will be included in the new icon object.  