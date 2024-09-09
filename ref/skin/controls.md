[]{#/{skin}/control}    
## controls (skin)    
**Control types:**    
:   [Bar](/ref/%7Bskin%7D/control/bar/bar.md): A progress bar or slider    
:   [Browser](/ref/%7Bskin%7D/control/browser/browser.md): A browser    
:   [Button](/ref/%7Bskin%7D/control/button/button.md): A pushbutton or toggle button    
:   [Child](/ref/%7Bskin%7D/control/child/child.md): A container holding one or two    
    panes, with a movable splitter    
:   [Grid](/ref/%7Bskin%7D/control/grid/grid.md): For table-like or list-like    
    output    
:   [Info](/ref/%7Bskin%7D/control/info/info.md): Classic BYOND statpanel    
:   [Input](/ref/%7Bskin%7D/control/input/input.md): Command input or other    
    user-entered text    
:   [Label](/ref/%7Bskin%7D/control/label/label.md): Non-interactive text label    
:   [Main](/ref/%7Bskin%7D/control/main/main.md): A window or pane that holds other    
    controls    
:   [Macro](/ref/%7Bskin%7D/control/macro/macro.md): A [keyboard/gamepad/mouse    
    macro](/ref/%7Bskin%7D/macros/macros.md)    
:   [Map](/ref/%7Bskin%7D/control/map/map.md): The game map display    
:   [Menu](/ref/%7Bskin%7D/control/menu/menu.md): An item in a drop-down menu    
:   [Output](/ref/%7Bskin%7D/control/output/output.md): Text output    
:   [Tab](/ref/%7Bskin%7D/control/tab/tab.md): A tab control holding multiple    
    panes, showing one at a time    
<!-- -->    
**Parameters common to all controls:**    
:   [id](/ref/%7Bskin%7D/param/id/id.md)    
:   [is-disabled](/ref/%7Bskin%7D/param/is-disabled/is-disabled.md)    
:   [parent](/ref/%7Bskin%7D/param/parent/parent.md)    
:   [saved-params](/ref/%7Bskin%7D/param/saved-params/saved-params.md)    
:   [type](/ref/%7Bskin%7D/param/type/type.md)    
**Positionable controls only (not Macro or Menu):**    
:   [anchor1, anchor2](/ref/%7Bskin%7D/param/anchor/anchor.md)    
:   [background-color](/ref/%7Bskin%7D/param/background-color/background-color.md)    
:   [border](/ref/%7Bskin%7D/param/border/border.md)    
:   [drop-zone](/ref/%7Bskin%7D/param/drop-zone/drop-zone.md)    
:   [flash](/ref/%7Bskin%7D/param/flash/flash.md)    
:   [focus](/ref/%7Bskin%7D/param/focus/focus.md)    
:   [font-family](/ref/%7Bskin%7D/param/font-family/font-family.md)    
:   [font-size](/ref/%7Bskin%7D/param/font-size/font-size.md)    
:   [font-style](/ref/%7Bskin%7D/param/font-style/font-style.md)    
:   [is-visible](/ref/%7Bskin%7D/param/is-visible/is-visible.md)    
:   [is-transparent](/ref/%7Bskin%7D/param/is-transparent/is-transparent.md)    
:   [on-size](/ref/%7Bskin%7D/param/on-size/on-size.md)    
:   [pos](/ref/%7Bskin%7D/param/pos/pos.md)    
:   [right-click](/ref/%7Bskin%7D/param/right-click/right-click.md)    
:   [size](/ref/%7Bskin%7D/param/size/size.md)    
:   [text-color](/ref/%7Bskin%7D/param/text-color/text-color.md)    
### Creating/Destroying at runtime    
Controls can be created or deleted at runtime. (Only controls you    
created during runtime may be deleted.) To create a control, call    
[winset()](/ref/proc/winset/winset.md){.code} using the    
[id](/ref/%7Bskin%7D/param/id/id.md){.code} of the new control, and the parameter    
list should include [type](/ref/%7Bskin%7D/param/type/type.md){.code},    
[parent](/ref/%7Bskin%7D/param/parent/parent.md){.code}, and probably also    
[pos](/ref/%7Bskin%7D/param/pos/pos.md){.code},    
[size](/ref/%7Bskin%7D/param/size/size.md){.code}, and any    
[anchors](/ref/%7Bskin%7D/param/anchor/anchor.md).    
To delete the control again, set its `parent` to a blank value.    
Menu items and macros work similarly, except they have no positional    
info. For those, the [name](/ref/%7Bskin%7D/param/name/name.md){.code} parameter is    
important when you create them, and you will either need    
[command](/ref/%7Bskin%7D/param/command/command.md){.code} or (for macros)    
[map-to](/ref/%7Bskin%7D/param/map-to/map-to.md){.code} to do anything with them.  