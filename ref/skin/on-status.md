## on-status parameter (skin)

<!-- -->
**Applies to:**
+   [Main](/ref/skin/control/main.md) 
<!-- -->
**Format:**
+   string


[Command](/ref/skin/commands.md)  executed when the text that
would go in the statusbar is changed. This applies even if this control
is a pane and not a window, or is a window without a statusbar. It
applies to all panes and windows that directly or indirectly contain
whatever control generated the statusbar text (e.g., a map). 

If
you include `[[*]]` in the command, it will be replaced by the new text.
(See "Embedded Winget" in [client commands](/ref/skin/commands.md) for
more details on the `[[...]]` format.) 

`[[from]]` can be used
to reference the control (if any) that generated the next text. You can
also use expressions like `[[from.type]]`, `[[from.parent.pos.x]]`, etc.

> [!TIP] 
> **See also:**
> +   [statusbar parameter](/ref/skin/param/statusbar.md) 