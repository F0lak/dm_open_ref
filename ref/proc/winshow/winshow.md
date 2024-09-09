[]{#/proc/winshow}    
## winshow proc    
**See also:**    
:   [winclone proc](ref/proc/winclone)    
:   [winget proc](ref/proc/winget)    
:   [winset proc](ref/proc/winset)    
:   [User interface skins](ref/%7Bskin%7D)    
:   [is-visible parameter (skin)](ref/%7Bskin%7D/param/is-visible)    
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