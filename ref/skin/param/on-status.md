
## on-status (info)
***
<a href="#/{skin}/commands">Command</a> executed when the text that would go in the statusbar is changed. This applies even if this control is a pane and not a window, or is a window without a statusbar. It applies to all panes and windows that directly or indirectly contain whatever control generated the statusbar text (e.g., a map).

If you include `[[*]]` in the command, it will be replaced by the new text. (See <a href="#/{skin}/commands/embed">embedded winget</a> for more details on the `[[...]]` format.)

`[[from]]` can be used to reference the control (if any) that generated the next text. You can also use expressions like `[[from.type]]`, `[[from.parent.pos.x]]`, etc.
***