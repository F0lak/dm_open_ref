
## is-default (info)
***
Specifies that this is a default control. This should be true for your main window, and for your primary map, info, output, input, and browser controls.

The default control of a given type can be referenced in <a class="code" href="#/proc/winset">winset()</a> and other skin-related procs by the name `":*type*"`, e.g. `":map"`.

Changing this value at runtime should be avoided, especially for windows. Results may be unpredictable.
***