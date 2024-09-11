## User interface skins
**See also:**
*   [winset proc](/ref/proc/winset.md) -m
*   [winget proc](/ref/proc/winget.md) -m
*   [output proc](/ref/proc/output.md) -m
*   [winclone proc](/ref/proc/winclone.md) -m
*   [winexists proc](/ref/proc/winexists.md) -m
*   [winshow proc](/ref/proc/winshow.md) -m
*   [controls](/ref/%7Bskin%7D/control.md) -m
*   [parameters](/ref/%7Bskin%7D/param.md) -m
*   [macros (skin)](/ref/%7Bskin%7D/macros.md) -m
*   [client commands](/ref/%7Bskin%7D/commands.md) -m


BYOND games used to have very limited interface options, all
effectively sharing the same layout. In BYOND 4.0, skins were
introduced, allowing developers more control over the layout. 

A
skin consists of [macro sets](/ref/%7Bskin%7D/macros.md) -m for keyboard/gamepad
input, menus, and windows and/or panes. All of these are considered
[controls](/ref/%7Bskin%7D/control.md) -m that a game can interact with via
[winset()](/ref/proc/winset.md) -m{.code}, [winget()](/ref/proc/winget.md) -m{.code},
[output()](/ref/proc/output.md) -m{.code}, and a few other procs. 

About
the simplest possible skin is a single window with a single [map
control](/ref/%7Bskin%7D/control/map.md) -m and a single macro set.