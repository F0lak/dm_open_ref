## macros (skin)


Macros are used to convert keyboard and gamepad events into
actions. There are two ways this works: A macro can run a command, or in
some cases (such as gamepad controls) it can be used to remap one
control to another. 

A collection of macros is called a macro
set, and the window currently in use defines which macro set will be
used via its [macro](/ref/%7Bskin%7D/param/macro.md) {.code} parameter.


Macros can be changed at runtime. If a macro does not have an
[id](/ref/%7Bskin%7D/param/id.md) {.code}, you can refer to it by its key
combination ([name](/ref/%7Bskin%7D/param/name.md) {.code}). If you have a
macro set named `macro1` and have a `Ctrl+E` macro for instance, you
could use [winset()](/ref/proc/winset.md) {.code} with `"macro1.Ctrl+E"`. See
the [Macro control](/ref/%7Bskin%7D/control/macro.md)  for information on which
parameters you can change with `winset()`. 

The `name` of the
macro is actually the full key combination as it would appear in the
macro editor, like `CTRL+E`, `Space+REP`, or `Alt+Shift+F1`. This is not
case-specific and it doesn\'t matter where you put modifiers like
`CTRL+`, `SHIFT+`, etc.
### The Any macro 
###### BYOND Version 511


Oftentimes it\'s desirable to keep track of key presses
yourself rather than have a hundred different macros defined. BYOND
makes this possible via the `Any` and `Any+UP` macros, which respond to
any key or gamepad button. `UP` is the only allowed modifier for this
macro, since other modifier keys are handled by this same macro.


Typically, you will want to use [set
instant=1](/ref/verb/set/instant.md) {.code} on the verbs that will be tied to
the Any macro, so that keyboard input doesn\'t queue up and lag behind.


In the [command](/ref/%7Bskin%7D/param/command.md) {.code} that goes
with this macro, `[[*]]` will be replaced with the name of the key or
gamepad button that was pressed/released. (See \"Embedded Winget\" in
[client commands](/ref/%7Bskin%7D/commands.md)  for more details on the
`[[...]]` format.)
### Mapping {#mapping byondver="511"}


The [map-to](/ref/%7Bskin%7D/param/map-to.md) {.code} parameter is
used by **mappings**, which are like macros but are used to convert
gamepad inputs easily and quickly to keyboard inputs. E.g.,
`GamepadLeft` can map to `West` which is the left arrow key. A set of
default mappings will be added automatically at runtime if you don\'t
include any gamepad mapping in your project.
### Gamepads {#gamepads byondver="511"}


BYOND will support up to four gamepads, and breaks up their
input into the following categories:
-   **Buttons:** Buttons on the controller that are either pressed or
    not pressed.
-   **Directions:** Directions pressed on the D-pad, which act like
    buttons. Diagonals are also included.
-   **D-pad:** The D-pad itself, which can be used to read a
    [dir](/ref/atom/var/dir.md) {.code} number.
-   **Analog:** The analog sticks (BYOND supports left and right).


See the list of available macros below for information on how
to harness these inputs. 

To let a user configure their gamepad,
you need to call the client-side `.gamepad-mapping`
[command](/ref/%7Bskin%7D/commands.md) . Or, if they have access to the Options
& Messages window and Dream Seeker\'s default menus, they can reach it
from there. However it\'s a good idea to make this easy for them to
find. Several common gamepads are already known by BYOND. 

There
is also the `GamepadRaw` macro, which is similar to `Any` in some ways
and will avoid doing any processing (e.g. checking for dead zones on the
analog sticks) so you can handle all input yourself. `GamepadRaw` does
not rely on BYOND\'s controller configuration, so it will not, for
instance, know that button 0 should be `GamepadFace1`. See below for
more information on how to use this macro.
### Mouse macros {#mouse-macros byondver="514"}


You can add macros (not local player-defined ones) for any of
the mouse input commands, thereby bypassing the normal mouse verbs. This
can be helpful for designing custom setups where you don\'t want to have
to parse the normal parameter string that provides most of the info, and
instead want to provide data directly to the verb. You will want
`set instant=1` on any such verb. 

Mouse macro commands use the
`[[...]]` syntax to embed values, just like [embedded
wingets](/ref/%7Bskin%7D/commands.md) . These are the values you can include in
a mouse macro:
  Embedded keyword                                                                                                               Meaning
  ------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------
  `action`                                                                                                                       Name of the mouse action (e.g. MouseDown, MouseMove, etc.).
  `src`                                                                                                                          Object the mouse is touching, or dragging/dropping.
  `loc`                                                                                                                          Turf or statpanel that `src` is over; in a drag-drop you should split this into `src.loc` and `over.loc`.
  `button`                                                                                                                       Mouse button used for this action, if any: `left`, `middle`, or `right`.
  `drag`                                                                                                                         Mouse button currently used for dragging.
  `buttons`                                                                                                                      Mouse buttons currently down or involved in this action, separated by commas.
  `keys`                                                                                                                         Modifier keys currently held (`shift`, `ctrl`, `alt`), separated by commas.
  `over`                                                                                                                         Object the mouse is over in a drag/drop operation.
  `id`                                                                                                                           Control ID; in a drag-drop you should split this into `src.id` and `over.id`.
  `icon`                                                                                                                         The icon offset (starting from 1,1 at the lower left) where the mouse action occurred.^\*^
  `tile`                                                                                                                         The tile where the mouse action occurred, if relevant.^\*^
  `vis`                                                                                                                          Pixel coordinates relative to the icon\'s position on screen (same as `icon` but without taking transform into account).^\*^
  `screen_loc`                                                                                                                   The regular `screen_loc` cordinate string.^\*^
  `screen`                                                                                                                       `screen_loc` coordinates but entirely in pixels starting at 0,0 from lower left.^\*^
  `screen_tile`                                                                                                                  `screen_loc` coordinates but only the tile number starting at 1,1.^\*^
  `screen_offset`                                                                                                                `screen_loc` coordinates but only the pixel offset from the tile, starting at 0,0.^\*^
  `delta`                                                                                                                        Wheel changes in a mouse wheel command.^\*^
  `left`, `right`, `middle`                                                                                                      1 if this button is down or involved in this action, 0 otherwise
  `shift`, `ctrl`, `alt`                                                                                                         1 if this modifier key is held, 0 otherwise
  `link`                                                                                                                         1 if the mouse is over a maptext link, 0 otherwise
  `cell`                                                                                                                         Grid cell involved in a mouse action. In a drag/drop action, `src.cell` is the dragging cell and `over.cell` is the drop cell.
  `drag-cell`                                                                                                                    Alias for `src.cell`.
  `drop-cell`                                                                                                                    Alias for `over.cell`.
  ^\*^ Coordinate values are comma-separated, but you can follow them with `.x` or `.y` to get the individual X and Y numbers.   


An example mouse macro command might look like this:
> my-mousedown-verb [[src]] [[button]] "keys=[[keys as params]];drag=[[drag as params]]"


And the verb to go with it looks like this: 
```
 client
// \"in src\" is the same as \"in usr.client\" here
verb/my_mousedown_verb(object as anything in src, button as text, params
as text) 
```
 

In the example, the `src` value is a
reference such as you would get with the [`ref()` proc](/ref/proc/ref.md) . It
can be used as a verb argument directly and won\'t be enclosed by quotes
by default. The `button` value is a string and the default formatting
will put quotes around it. The `keys` and `drag` values were given the
`as params` format specifier so they would behave as part of a
[parameter list](/ref/proc/list2params.md)  

In drag/drop actions, you
can precede any value with `src` or `over` if there may be different
information for the dragged object and the mouseover object/location.
This also applies to things like `keys`, which by default will be the
currently held keys but you can use `src.keys` to refer to the values
from when the drag began.
### Available macros


This is a list of all keys and gamepad events that can be used
in macros.
**Macro modifiers** are part of the macro name, and control the
conditions in which the macro will fire.
Modifier
Meaning
`SHIFT+`
This macro only counts if either Shift key is pressed.
`CTRL+`
This macro only counts if either Ctrl key is pressed.
`ALT+`
This macro only counts if either Alt key is pressed.
`+REP`
If a key/button is held down, this macro repeats.
`+UP`
This macro fires when the key/button is released.
**Keyboard keys** are the garden-variety macros. (This list is abridged
to exclude keys probably no one has.)
Key
Description
`A` - `Z`
Letter key
`0` - `9`
Number key
`Numpad0` - `Numpad9`
Numpad numbers
`North`
Up arrow
`South`
Down arrow
`East`
Right arrow
`West`
Left arrow
`Northwest`
Home key
`Southwest`
End key
`Northeast`
Page Up key
`Southeast`
Page Down key
`Center`
Center key (numpad)
`Return`
Enter / Return key
`Escape`
Esc key
`Tab`
Tab key
`Space`
Space bar
`Back`
Backspace key
`Insert`
Ins key
`Delete`
Del key
`Pause`
Pause key
`Snapshot`
Snapshot / Print Screen key
`LWin`
Left Windows key
`RWin`
Right Windows key
`Apps`
Apps key
`Multiply`
Multiply key
`Add`
Add key
`Subtract`
Subtract key
`Divide`
Divide / Slash key
`Separator`
Separator / Backslash key
`Shift`
Shift key (when not used as a modifier)
`Ctrl`
Ctrl key (when not used as a modifier)
`Alt`
Alt key (when not used as a modifier)
`VolumeMute`
Mute key
`VolumeUp`
Volume up key
`VolumeDown`
Volume down key
`MediaPlayPause`
Play/pause media key
`MediaStop`
Stop media key
`MediaNext`
Next track key
`MediaPrev`
Previous track key
**Special macros**
**`Any`**
A special macro that can run a command on press/release of any key or
gamepad button. `UP` is the only modifier allowed. In the command,
`[[*]]` is replaced with the key/button name.^\*^
**`GamepadRaw`**^\*^
Captures raw input from a gamepad, without regard to the adjustments
done by the Gamepad Setup dialog. In the command, `[[id]]` is replaced
by the name of the button or axis changed (\"Button0\" through
\"Button15\" and \"Axis0\" through \"Axis11\"), `[[value]]` is replaced
with the value of the button or axis, and `[[*]]` is equivalent to
`[[id]] [[value]]`.


^\*^ If no gamepad mappings are included in a game\'s
interface, the default mappings are used instead, which will map the
Dpad buttons to the arrow keys. This will cause the Any macro to
register both a gamepad directional button and the mapped key on the
same press. If you plan on using macros to capture gamepad input, you
may wish instead to map any one of the directional buttons to \"None\",
which will override the default gamepad mappings completely.
**Gamepad buttons**^†^ can use another gamepad button as a modifier (but
not CTRL, SHIFT, ALT), and can be mapped to one or two keyboard keys or
mouse buttons.
Button
Description
`GamepadFace1`
A (Xbox), X (PS), bottom of diamond
`GamepadFace2`
B (Xbox), Circle (PS), right of diamond
`GamepadFace3`
X (Xbox), Square (PS), left of diamond
`GamepadFace4`
Y (Xbox), Triangle (PS), top of diamond
`GamepadL1`
Left top shoulder
`GamepadR1`
Right top shoulder
`GamepadL2`
Left bottom shoulder
`GamepadR2`
Right bottom shoulder
`GamepadSelect`
Select / Back
`GamepadStart`
Start / Forward
`GamepadL3`
Left analog click
`GamepadR3`
Right analog click
Directional buttons: only one can pressed at a time, and the diagonal
buttons are virtual.
`GamepadUp`
Up button
`GamepadDown`
Down button
`GamepadLeft`
Left button
`GamepadRight`
Right button
`GamepadUpLeft`
Up+left virtual button
`GamepadUpRight`
Up+right virtual button
`GamepadDownLeft`
Down+left virtual button
`GamepadDownRight`
Down+right virtual button
**Gamepad analog sticks**^†^ can have commands and/or map to
`GamepadDir`, `GamepadDir4`, or `Mouse`. They can use a gamepad button
as a modifier. In a command, `[[x]]` and `[[y]]` are replaced by
coordinates, and `[[*]]` is replaced by both with a comma for
separation.
`GamepadLeftAnalog`
Left analog stick
`GamepadRightAnalog`
Left analog stick
**Gamepad Dpads**^†‡^ can have commands or are used as mapping targets
for analog sticks. A gamepad button can be used as a modifier. In a
command, `[[*]]` is replaced by a direction number, which can be 0.
`GamepadDir`
Dpad, converted to one of the eight standard directions.
`GamepadDir4`
Dpad, converted to a cardinal direction.


^†^ All of the gamepad macros defined above apply to the first
gamepad. BYOND can now support up to four gamepads, and you can replace
Gamepad in the names above with Gamepad2, Gamepad3, or Gamepad4 to
access them. Each gamepad also has its own raw macro (i.e.,
Gamepad2Raw).


^‡^ If you use a Dpad macro like GamepadDir as a `map-to`
target, you don\'t have to specify gamepad 2-4 in map-to; the mapping
will automatically know that when Gamepad2LeftAnalog is mapped to
GamepadDir, it means Gamepad2Dir.
**Mouse macros** can have commands but not be used as mapping targets.
`MouseDown`
Mouse button pressed (replaces MouseDown verb)
`MouseUp`
Mouse button released (replaces MouseUp verb)
`MouseClick`
A click action has occurred (replaces Click verb)
`MouseDblClick`
A double-click action has occurred (replaces DblClick verb)
`MouseOver`
Mouse has moved over a new icon or entered/exited a control (replaces
MouseEntered and MouseExited verbs)
`MouseMove`
Mouse has moved to a new pixel of the same icon (replaces MouseMove
verb)
`MouseDrag`
Mouse has begin dragging or is over a new drop target (replaces
MouseDrag verb)
`MouseDragMove`
Mouse is dragging and is over a new pixel of the same drop target
(replaces MouseDrag verb in situations where MouseMove would apply)
`MouseDrop`
Mouse drag has been released over a target (replaces MouseDrop verb)
`MouseWheel`
A wheel movement has occurred (replaces MouseWheel verb)
**Mouse targets** can only be used as mapping targets for another macro.
`Mouse`
The mouse cursor, mappable by a gamepad analog stick.
`MouseLeftButton`
Left button, mappable by a gamepad button.
`MouseRightButton`
Right button, mappable by a gamepad button.
`MouseMiddleButton`
Middle button, mappable by a gamepad button.

