[]{#/{skin}/param/on-size}    
## on-size parameter (skin) {#on-size-parameter-skin byondver="482"}    
**See also:**    
:   [size parameter](/ref/%7Bskin%7D/param/size/size.md)    
<!-- -->    
**Applies to:**    
:   [All](/ref/%7Bskin%7D/control/control.md)    
<!-- -->    
**Format:**    
:   string    
[Command](/ref/%7Bskin%7D/commands/commands.md) executed when this control is resized.    
If you are dragging a window edge or splitter, the command won\'t run    
until you finish.    
No command will be sent in response to size or splitter changes made by    
[winset()](/ref/proc/winset/winset.md){.code}.    
If you include `[[*]]` in the command, it will be replaced by the    
control\'s new size. Likewise, `[[width]]` will be replaced with the    
width and `[[height]]` with the height. (See \"Embedded Winget\" in    
[client commands](/ref/%7Bskin%7D/commands/commands.md) for more details on the    
`[[...]]` format.)  