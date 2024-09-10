[]{#/winshow proc.md}    
## winshow proc    
**See also:**    
:   [winclone proc](/proc/winclone)    
:   [winget proc](/proc/winget)    
:   [winset proc](/proc/winset)    
:   [User interface skins](/%7Bskin%7D)    
:   [is-visible parameter (skin)](/%7Bskin%7D/param/is-visible)    
<!-- -->    
**Format:**    
:   winshow(player, window, show=1)    
<!-- -->    
**Args:**    
:   player: A mob or client.    
:   window: The name of a window in the player\'s skin.    
:   show: Use a nonzero value to show the window, zero to hide it.    
Shows or hides a window in the player\'s skin. This is a shortcut,    
equivalent to setting `is-visible` via `winset()`.  