
## macros (info)
***
Macros are used to convert keyboard and gamepad events into actions. There are two ways this works: A macro can run a command, or in some cases (such as gamepad controls) it can be used to remap one control to another.

A collection of macros is called a macro set, and the window currently in use defines which macro set will be used via its <a class="code" href="#/{skin}/param/macro">macro</a> parameter.

Macros can be changed at runtime. If a macro does not have an <a class="code" href="#/{skin}/param/id">id</a>, you can refer to it by its key combination (<a class="code" href="#/{skin}/param/name">name</a>). If you have a macro set named `macro1` and have a `Ctrl+E` macro for instance, you could use <a class="code" href="#/proc/winset">winset()</a> with `"macro1.Ctrl+E"`. See the <a href="#/{skin}/control/macro">Macro control</a> for information on which parameters you can change with `winset()`.

The `name` of the macro is actually the full key combination as it would appear in the macro editor, like `CTRL+E`, `Space+REP`, or `Alt+Shift+F1`. This is not case-specific and it doesn't matter where you put modifiers like `CTRL+`, `SHIFT+`, etc.

Oftentimes it's desirable to keep track of key presses yourself rather than have a hundred different macros defined. BYOND makes this possible via the `Any` and `Any+UP` macros, which respond to any key or gamepad button. `UP` is the only allowed modifier for this macro, since other modifier keys are handled by this same macro.

Typically, you will want to use <a class="code" href="#/verb/set/instant">set instant=1</a> on the verbs that will be tied to the Any macro, so that keyboard input doesn't queue up and lag behind.

In the <a class="code" href="#/{skin}/param/command">command</a> that goes with this macro, `[[*]]` will be replaced with the name of the key or gamepad button that was pressed/released. (See <a href="#/{skin}/commands/embed">embedded winget</a> for more details on the `[[...]]` format.)

The <a class="code" href="#/{skin}/param/map-to">map-to</a> parameter is used by **mappings**, which are like macros but are used to convert gamepad inputs easily and quickly to keyboard inputs. E.g., `GamepadLeft` can map to `West` which is the left arrow key. A set of default mappings will be added automatically at runtime if you don't include any gamepad mapping in your project.

BYOND will support up to four gamepads, and breaks up their input into the following categories:

See the list of available macros below for information on how to harness these inputs.

To let a user configure their gamepad, you need to call the client-side `.gamepad-mapping` <a href="#/{skin}/commands">command</a>. Or, if they have access to the Options &amp; Messages window and Dream Seeker's default menus, they can reach it from there. However it's a good idea to make this easy for them to find. Several common gamepads are already known by BYOND.

There is also the `GamepadRaw` macro, which is similar to `Any` in some ways and will avoid doing any processing (e.g. checking for dead zones on the analog sticks) so you can handle all input yourself. `GamepadRaw` does not rely on BYOND's controller configuration, so it will not, for instance, know that button 0 should be `GamepadFace1`. See below for more information on how to use this macro.

You can add macros (not local player-defined ones) for any of the mouse input commands, thereby bypassing the normal mouse verbs. This can be helpful for designing custom setups where you don't want to have to parse the normal parameter string that provides most of the info, and instead want to provide data directly to the verb. You will want `set instant=1` on any such verb.

Mouse macro commands use the `[[...]]` syntax to embed values, just like <a href="#/{skin}/commands/embed">embedded wingets</a>. These are the values you can include in a mouse macro:
***