[]{#/controls (skin).md}/control}    
## controls (skin)    
**Control types:**    
:   [Bar](/%7Bskin%7D/control/bar): A progress bar or slider    
:   [Browser](/%7Bskin%7D/control/browser): A browser    
:   [Button](/%7Bskin%7D/control/button): A pushbutton or toggle button    
:   [Child](/%7Bskin%7D/control/child): A container holding one or two    
    panes, with a movable splitter    
:   [Grid](/%7Bskin%7D/control/grid): For table-like or list-like    
    output    
:   [Info](/%7Bskin%7D/control/info): Classic BYOND statpanel    
:   [Input](/%7Bskin%7D/control/input): Command input or other    
    user-entered text    
:   [Label](/%7Bskin%7D/control/label): Non-interactive text label    
:   [Main](/%7Bskin%7D/control/main): A window or pane that holds other    
    controls    
:   [Macro](/%7Bskin%7D/control/macro): A [keyboard/gamepad/mouse    
    macro](/%7Bskin%7D/macros)    
:   [Map](/%7Bskin%7D/control/map): The game map display    
:   [Menu](/%7Bskin%7D/control/menu): An item in a drop-down menu    
:   [Output](/%7Bskin%7D/control/output): Text output    
:   [Tab](/%7Bskin%7D/control/tab): A tab control holding multiple    
    panes, showing one at a time    
<!-- -->    
**Parameters common to all controls:**    
:   [id](/%7Bskin%7D/param/id)    
:   [is-disabled](/%7Bskin%7D/param/is-disabled)    
:   [parent](/%7Bskin%7D/param/parent)    
:   [saved-params](/%7Bskin%7D/param/saved-params)    
:   [type](/%7Bskin%7D/param/type)    
**Positionable controls only (not Macro or Menu):**    
:   [anchor1, anchor2](/%7Bskin%7D/param/anchor)    
:   [background-color](/%7Bskin%7D/param/background-color)    
:   [border](/%7Bskin%7D/param/border)    
:   [drop-zone](/%7Bskin%7D/param/drop-zone)    
:   [flash](/%7Bskin%7D/param/flash)    
:   [focus](/%7Bskin%7D/param/focus)    
:   [font-family](/%7Bskin%7D/param/font-family)    
:   [font-size](/%7Bskin%7D/param/font-size)    
:   [font-style](/%7Bskin%7D/param/font-style)    
:   [is-visible](/%7Bskin%7D/param/is-visible)    
:   [is-transparent](/%7Bskin%7D/param/is-transparent)    
:   [on-size](/%7Bskin%7D/param/on-size)    
:   [pos](/%7Bskin%7D/param/pos)    
:   [right-click](/%7Bskin%7D/param/right-click)    
:   [size](/%7Bskin%7D/param/size)    
:   [text-color](/%7Bskin%7D/param/text-color)    
### Creating/Destroying at runtime    
Controls can be created or deleted at runtime. (Only controls you    
created during runtime may be deleted.) To create a control, call    
[winset()](/proc/winset){.code} using the    
[id](/%7Bskin%7D/param/id){.code} of the new control, and the parameter    
list should include [type](/%7Bskin%7D/param/type){.code},    
[parent](/%7Bskin%7D/param/parent){.code}, and probably also    
[pos](/%7Bskin%7D/param/pos){.code},    
[size](/%7Bskin%7D/param/size){.code}, and any    
[anchors](/%7Bskin%7D/param/anchor).    
To delete the control again, set its `parent` to a blank value.    
Menu items and macros work similarly, except they have no positional    
info. For those, the [name](/%7Bskin%7D/param/name){.code} parameter is    
important when you create them, and you will either need    
[command](/%7Bskin%7D/param/command){.code} or (for macros)    
[map-to](/%7Bskin%7D/param/map-to){.code} to do anything with them.  