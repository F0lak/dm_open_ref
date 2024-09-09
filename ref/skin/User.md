[]{#/{skin} toc="User interface skins"}    
## User interface skins    
**See also:**    
:   [winset proc](/ref/proc/winset/winset.md)    
:   [winget proc](/ref/proc/winget/winget.md)    
:   [output proc](/ref/proc/output/output.md)    
:   [winclone proc](/ref/proc/winclone/winclone.md)    
:   [winexists proc](/ref/proc/winexists/winexists.md)    
:   [winshow proc](/ref/proc/winshow/winshow.md)    
:   [controls](/ref/%7Bskin%7D/control/control.md)    
:   [parameters](/ref/%7Bskin%7D/param/param.md)    
:   [macros (skin)](/ref/%7Bskin%7D/macros/macros.md)    
:   [client commands](/ref/%7Bskin%7D/commands/commands.md)    
BYOND games used to have very limited interface options, all effectively    
sharing the same layout. In BYOND 4.0, skins were introduced, allowing    
developers more control over the layout.    
A skin consists of [macro sets](/ref/%7Bskin%7D/macros/macros.md) for    
keyboard/gamepad input, menus, and windows and/or panes. All of these    
are considered [controls](/ref/%7Bskin%7D/control/control.md) that a game can interact    
with via [winset()](/ref/proc/winset/winset.md){.code},    
[winget()](/ref/proc/winget/winget.md){.code}, [output()](/ref/proc/output/output.md){.code}, and    
a few other procs.    
About the simplest possible skin is a single window with a single [map    
control](/ref/%7Bskin%7D/control/map/map.md), and a single macro set.  