[]{#/{skin}/param/on-change}    
## on-change parameter (skin)    
**See also:**    
:   [value parameter](/ref/%7Bskin%7D/param/value/value.md)    
<!-- -->    
**Applies to:**    
:   [Bar](/ref/%7Bskin%7D/control/bar/bar.md)    
<!-- -->    
**Format:**    
:   string    
[Command](/ref/%7Bskin%7D/commands/commands.md) executed when the    
[value](/ref/%7Bskin%7D/param/value/value.md){.code} of the bar/slider is changed.    
If you drag the slider around, the command will not run until you let    
go.    
If you include `[[*]]` in the command, it will be replaced by the    
control\'s new `value`. (See \"Embedded Winget\" in [client    
commands](/ref/%7Bskin%7D/commands/commands.md) for more details on the `[[...]]`    
format.)  