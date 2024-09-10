[]{#/User interface skins.md} toc="User interface skins"}    
## User interface skins    
**See also:**    
:   [winset proc](/proc/winset)    
:   [winget proc](/proc/winget)    
:   [output proc](/proc/output)    
:   [winclone proc](/proc/winclone)    
:   [winexists proc](/proc/winexists)    
:   [winshow proc](/proc/winshow)    
:   [controls](/%7Bskin%7D/control)    
:   [parameters](/%7Bskin%7D/param)    
:   [macros (skin)](/%7Bskin%7D/macros)    
:   [client commands](/%7Bskin%7D/commands)    
BYOND games used to have very limited interface options, all effectively    
sharing the same layout. In BYOND 4.0, skins were introduced, allowing    
developers more control over the layout.    
A skin consists of [macro sets](/%7Bskin%7D/macros) for    
keyboard/gamepad input, menus, and windows and/or panes. All of these    
are considered [controls](/%7Bskin%7D/control) that a game can interact    
with via [winset()](/proc/winset){.code},    
[winget()](/proc/winget){.code}, [output()](/proc/output){.code}, and    
a few other procs.    
About the simplest possible skin is a single window with a single [map    
control](/%7Bskin%7D/control/map), and a single macro set.  