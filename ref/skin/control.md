## controls (skin)
**Control types:**
*   [Bar](/ref/%7Bskin%7D/control/bar.md) -m* A progress bar or slider
*   [Browser](/ref/%7Bskin%7D/control/browser.md) -m* A browser
*   [Button](/ref/%7Bskin%7D/control/button.md) -m* A pushbutton or toggle button
*   [Child](/ref/%7Bskin%7D/control/child.md) -m* A container holding one or two
    panes, with a movable splitter
*   [Grid](/ref/%7Bskin%7D/control/grid.md) -m* For table-like or list-like
    output
*   [Info](/ref/%7Bskin%7D/control/info.md) -m* Classic BYOND statpanel
*   [Input](/ref/%7Bskin%7D/control/input.md) -m* Command input or other
    user-entered text
*   [Label](/ref/%7Bskin%7D/control/label.md) -m* Non-interactive text label
*   [Main](/ref/%7Bskin%7D/control/main.md) -m* A window or pane that holds other
    controls
*   [Macro](/ref/%7Bskin%7D/control/macro.md) -m* A [keyboard/gamepad/mouse
    macro](/ref/%7Bskin%7D/macros.md) -m
*   [Map](/ref/%7Bskin%7D/control/map.md) -m* The game map display
*   [Menu](/ref/%7Bskin%7D/control/menu.md) -m* An item in a drop-down menu
*   [Output](/ref/%7Bskin%7D/control/output.md) -m* Text output
*   [Tab](/ref/%7Bskin%7D/control/tab.md) -m* A tab control holding multiple
    panes, showing one at a time
<!-- -->
**Parameters common to all controls:**
*   [id](/ref/%7Bskin%7D/param/id.md) -m
*   [is-disabled](/ref/%7Bskin%7D/param/is-disabled.md) -m
*   [parent](/ref/%7Bskin%7D/param/parent.md) -m
*   [saved-params](/ref/%7Bskin%7D/param/saved-params.md) -m
*   [type](/ref/%7Bskin%7D/param/type.md) -m
**Positionable controls only (not Macro or Menu):**
*   [anchor1, anchor2](/ref/%7Bskin%7D/param/anchor.md) -m
*   [background-color](/ref/%7Bskin%7D/param/background-color.md) -m
*   [border](/ref/%7Bskin%7D/param/border.md) -m
*   [drop-zone](/ref/%7Bskin%7D/param/drop-zone.md) -m
*   [flash](/ref/%7Bskin%7D/param/flash.md) -m
*   [focus](/ref/%7Bskin%7D/param/focus.md) -m
*   [font-family](/ref/%7Bskin%7D/param/font-family.md) -m
*   [font-size](/ref/%7Bskin%7D/param/font-size.md) -m
*   [font-style](/ref/%7Bskin%7D/param/font-style.md) -m
*   [is-visible](/ref/%7Bskin%7D/param/is-visible.md) -m
*   [is-transparent](/ref/%7Bskin%7D/param/is-transparent.md) -m
*   [on-size](/ref/%7Bskin%7D/param/on-size.md) -m
*   [pos](/ref/%7Bskin%7D/param/pos.md) -m
*   [right-click](/ref/%7Bskin%7D/param/right-click.md) -m
*   [size](/ref/%7Bskin%7D/param/size.md) -m
*   [text-color](/ref/%7Bskin%7D/param/text-color.md) -m
### Creating/Destroying at runtime


Controls can be created or deleted at runtime. (Only controls
you created during runtime may be deleted.) To create a control, call
[winset()](/ref/proc/winset.md) -m{.code} using the
[id](/ref/%7Bskin%7D/param/id.md) -m{.code} of the new control, and the parameter
list should include [type](/ref/%7Bskin%7D/param/type.md) -m{.code},
[parent](/ref/%7Bskin%7D/param/parent.md) -m{.code}, and probably also
[pos](/ref/%7Bskin%7D/param/pos.md) -m{.code},
[size](/ref/%7Bskin%7D/param/size.md) -m{.code}, and any
[anchors](/ref/%7Bskin%7D/param/anchor.md) -m. 

To delete the control
again, set its `parent` to a blank value. 

Menu items and macros
work similarly, except they have no positional info. For those, the
[name](/ref/%7Bskin%7D/param/name.md) -m{.code} parameter is important when you
create them, and you will either need
[command](/ref/%7Bskin%7D/param/command.md) -m{.code} or (for macros)
[map-to](/ref/%7Bskin%7D/param/map-to.md) -m.code} to do anything with them.