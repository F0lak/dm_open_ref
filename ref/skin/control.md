## controls (skin)
**Control types:**
+   [Bar](/ref/skin/control/bar.md) : A progress bar or slider
+   [Browser](/ref/skin/control/browser.md) : A browser
+   [Button](/ref/skin/control/button.md) : A pushbutton or toggle button
+   [Child](/ref/skin/control/child.md) : A container holding one or two
    panes, with a movable splitter
+   [Grid](/ref/skin/control/grid.md) : For table-like or list-like
    output
+   [Info](/ref/skin/control/info.md) : Classic BYOND statpanel
+   [Input](/ref/skin/control/input.md) : Command input or other
    user-entered text
+   [Label](/ref/skin/control/label.md) : Non-interactive text label
+   [Main](/ref/skin/control/main.md) : A window or pane that holds other
    controls
+   [Macro](/ref/skin/control/macro.md) : A [keyboard/gamepad/mouse
    macro](/ref/skin/macros.md) 
+   [Map](/ref/skin/control/map.md) : The game map display
+   [Menu](/ref/skin/control/menu.md) : An item in a drop-down menu
+   [Output](/ref/skin/control/output.md) : Text output
+   [Tab](/ref/skin/control/tab.md) : A tab control holding multiple
    panes, showing one at a time

**Parameters common to all controls:**
+   [id](/ref/skin/param/id.md) 
+   [is-disabled](/ref/skin/param/is-disabled.md) 
+   [parent](/ref/skin/param/parent.md) 
+   [saved-params](/ref/skin/param/saved-params.md) 
+   [type](/ref/skin/param/type.md) 
**Positionable controls only (not Macro or Menu):**
+   [anchor1, anchor2](/ref/skin/param/anchor.md) 
+   [background-color](/ref/skin/param/background-color.md) 
+   [border](/ref/skin/param/border.md) 
+   [drop-zone](/ref/skin/param/drop-zone.md) 
+   [flash](/ref/skin/param/flash.md) 
+   [focus](/ref/skin/param/focus.md) 
+   [font-family](/ref/skin/param/font-family.md) 
+   [font-size](/ref/skin/param/font-size.md) 
+   [font-style](/ref/skin/param/font-style.md) 
+   [is-visible](/ref/skin/param/is-visible.md) 
+   [is-transparent](/ref/skin/param/is-transparent.md) 
+   [on-size](/ref/skin/param/on-size.md) 
+   [pos](/ref/skin/param/pos.md) 
+   [right-click](/ref/skin/param/right-click.md) 
+   [size](/ref/skin/param/size.md) 
+   [text-color](/ref/skin/param/text-color.md) 
### Creating/Destroying at runtime


Controls can be created or deleted at runtime. (Only controls
you created during runtime may be deleted.) To create a control, call
[winset()](/ref/proc/winset.md)  using the
[id](/ref/skin/param/id.md)  of the new control, and the parameter
list should include [type](/ref/skin/param/type.md) ,
[parent](/ref/skin/param/parent.md) , and probably also
[pos](/ref/skin/param/pos.md) ,
[size](/ref/skin/param/size.md) , and any
[anchors](/ref/skin/param/anchor.md) . 

To delete the control
again, set its `parent` to a blank value. 

Menu items and macros
work similarly, except they have no positional info. For those, the
[name](/ref/skin/param/name.md)  parameter is important when you
create them, and you will either need
[command](/ref/skin/param/command.md)  or (for macros)
[map-to](/ref/skin/param/map-to.md) to do anything with them.