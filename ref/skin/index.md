
## {skin} (info)
***
BYOND games used to have very limited interface options, all effectively sharing the same layout. In BYOND 4.0, skins were introduced, allowing developers more control over the layout.

A skin consists of <a href="#/{skin}/macros">macro sets</a> for keyboard/gamepad input, menus, and windows and/or panes. All of these are considered <a href="#/{skin}/control">controls</a> that a game can interact with via <a class="code" href="#/proc/winset">winset()</a>, <a class="code" href="#/proc/winget">winget()</a>, <a class="code" href="#/proc/output">output()</a>, and a few other procs.

About the simplest possible skin is a single window with a single <a href="#/{skin}/control/map">map control</a>, and a single macro set.
***