## on-change parameter (skin)


**Applies to:**
+   [Bar](/ref/skin/control/bar.md) 

**Format:**
+   string


[Command](/ref/skin/commands.md)  executed when the
[value](/ref/skin/param/value.md)  of the bar/slider is changed.
If you drag the slider around, the command will not run until you let
go. 

If you include `[[*]]` in the command, it will be replaced
by the control\'s new `value`. (See "Embedded Winget" in [client
commands](/ref/skin/commands.md) for more details on the `[[...]]`
format.)

> [!TIP] 
> **See also:**
> +   [value parameter](/ref/skin/param/value.md) 