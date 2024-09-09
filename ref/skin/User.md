[]{#/{skin} toc="User interface skins"}    
## User interface skins    
**See also:**    
:   [winset proc](/ref/proc/winset)    
:   [winget proc](/ref/proc/winget)    
:   [output proc](/ref/proc/output)    
:   [winclone proc](/ref/proc/winclone)    
:   [winexists proc](/ref/proc/winexists)    
:   [winshow proc](/ref/proc/winshow)    
:   [controls](/ref/%7Bskin%7D/control)    
:   [parameters](/ref/%7Bskin%7D/param)    
:   [macros (skin)](/ref/%7Bskin%7D/macros)    
:   [client commands](/ref/%7Bskin%7D/commands)    
BYOND games used to have very limited interface options, all effectively    
sharing the same layout. In BYOND 4.0, skins were introduced, allowing    
developers more control over the layout.    
A skin consists of [macro sets](/ref/%7Bskin%7D/macros) for    
keyboard/gamepad input, menus, and windows and/or panes. All of these    
are considered [controls](/ref/%7Bskin%7D/control) that a game can interact    
with via [winset()](/ref/proc/winset){.code},    
[winget()](/ref/proc/winget){.code}, [output()](/ref/proc/output){.code}, and    
a few other procs.    
About the simplest possible skin is a single window with a single [map    
control](/ref/%7Bskin%7D/control/map), and a single macro set.  