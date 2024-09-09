[]{#/{skin}/control}    
## controls (skin)    
**Control types:**    
:   [Bar](/ref/%7Bskin%7D/control/bar): A progress bar or slider    
:   [Browser](/ref/%7Bskin%7D/control/browser): A browser    
:   [Button](/ref/%7Bskin%7D/control/button): A pushbutton or toggle button    
:   [Child](/ref/%7Bskin%7D/control/child): A container holding one or two    
    panes, with a movable splitter    
:   [Grid](/ref/%7Bskin%7D/control/grid): For table-like or list-like    
    output    
:   [Info](/ref/%7Bskin%7D/control/info): Classic BYOND statpanel    
:   [Input](/ref/%7Bskin%7D/control/input): Command input or other    
    user-entered text    
:   [Label](/ref/%7Bskin%7D/control/label): Non-interactive text label    
:   [Main](/ref/%7Bskin%7D/control/main): A window or pane that holds other    
    controls    
:   [Macro](/ref/%7Bskin%7D/control/macro): A [keyboard/gamepad/mouse    
    macro](/ref/%7Bskin%7D/macros)    
:   [Map](/ref/%7Bskin%7D/control/map): The game map display    
:   [Menu](/ref/%7Bskin%7D/control/menu): An item in a drop-down menu    
:   [Output](/ref/%7Bskin%7D/control/output): Text output    
:   [Tab](/ref/%7Bskin%7D/control/tab): A tab control holding multiple    
    panes, showing one at a time    
<!-- -->    
**Parameters common to all controls:**    
:   [id](/ref/%7Bskin%7D/param/id)    
:   [is-disabled](/ref/%7Bskin%7D/param/is-disabled)    
:   [parent](/ref/%7Bskin%7D/param/parent)    
:   [saved-params](/ref/%7Bskin%7D/param/saved-params)    
:   [type](/ref/%7Bskin%7D/param/type)    
**Positionable controls only (not Macro or Menu):**    
:   [anchor1, anchor2](/ref/%7Bskin%7D/param/anchor)    
:   [background-color](/ref/%7Bskin%7D/param/background-color)    
:   [border](/ref/%7Bskin%7D/param/border)    
:   [drop-zone](/ref/%7Bskin%7D/param/drop-zone)    
:   [flash](/ref/%7Bskin%7D/param/flash)    
:   [focus](/ref/%7Bskin%7D/param/focus)    
:   [font-family](/ref/%7Bskin%7D/param/font-family)    
:   [font-size](/ref/%7Bskin%7D/param/font-size)    
:   [font-style](/ref/%7Bskin%7D/param/font-style)    
:   [is-visible](/ref/%7Bskin%7D/param/is-visible)    
:   [is-transparent](/ref/%7Bskin%7D/param/is-transparent)    
:   [on-size](/ref/%7Bskin%7D/param/on-size)    
:   [pos](/ref/%7Bskin%7D/param/pos)    
:   [right-click](/ref/%7Bskin%7D/param/right-click)    
:   [size](/ref/%7Bskin%7D/param/size)    
:   [text-color](/ref/%7Bskin%7D/param/text-color)    
### Creating/Destroying at runtime    
Controls can be created or deleted at runtime. (Only controls you    
created during runtime may be deleted.) To create a control, call    
[winset()](/ref/proc/winset){.code} using the    
[id](/ref/%7Bskin%7D/param/id){.code} of the new control, and the parameter    
list should include [type](/ref/%7Bskin%7D/param/type){.code},    
[parent](/ref/%7Bskin%7D/param/parent){.code}, and probably also    
[pos](/ref/%7Bskin%7D/param/pos){.code},    
[size](/ref/%7Bskin%7D/param/size){.code}, and any    
[anchors](/ref/%7Bskin%7D/param/anchor).    
To delete the control again, set its `parent` to a blank value.    
Menu items and macros work similarly, except they have no positional    
info. For those, the [name](/ref/%7Bskin%7D/param/name){.code} parameter is    
important when you create them, and you will either need    
[command](/ref/%7Bskin%7D/param/command){.code} or (for macros)    
[map-to](/ref/%7Bskin%7D/param/map-to){.code} to do anything with them.  