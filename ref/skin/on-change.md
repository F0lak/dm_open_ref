[]{#/{skin}/param/on-change}
## on-change parameter (skin)
**See also:**
:   [value parameter](#/%7Bskin%7D/param/value)
<!-- -->
**Applies to:**
:   [Bar](#/%7Bskin%7D/control/bar)
<!-- -->
**Format:**
:   string
[Command](#/%7Bskin%7D/commands) executed when the
[value](#/%7Bskin%7D/param/value){.code} of the bar/slider is changed.
If you drag the slider around, the command will not run until you let
go.
If you include `[[*]]` in the command, it will be replaced by the
control\'s new `value`. (See \"Embedded Winget\" in [client
commands](#/%7Bskin%7D/commands) for more details on the `[[...]]`
format.)