[]{#/client commands.md}/commands}    
## client commands    
Several commands can be executed on the client that are not verbs, but    
instructions for Dream Seeker. Some of these commands have detailed    
syntax described in their own reference entries.    
[.winset](/%7Bskin%7D/commands/.winset)    
:   Sets skin parameters, and includes special syntax for conditional    
    actions.    
[.output](/%7Bskin%7D/commands/.output)    
:   Sends output to a control.    
.options    
:   Shows the Options & Messages box.    
.reboot    
:   Reboots the world, when Dream Seeker is also acting as a server.    
.reconnect    
:   Reconnects to the same world.    
.host    
:   Opens hosting options box, when Dream Seeker is also acting as a    
    server.    
.profile    
:   Opens the profiler. On a remote connection you may not have access    
    to profile server procs, but you can look at the client and network    
    profilers.    
.screenshot    
:   Saves a screenshot of the map. If there\'s more than one map    
    control, the default map is used.    
.screenshot auto    
:   Saves a screenshot of the map, but does not prompt for a filename.    
    The file will be saved in the client\'s user directory in    
    BYOND/screenshots.    
.gamepad-mapping    
:   Opens the gamepad mapping dialog. Helpful if the user\'s gamepad is    
    not supported or not configured to their liking.    
.command    
:   Prompts the user to enter a command, which can be one of these    
    commands as well.    
[.sound](/%7Bskin%7D/commands/sound)    
:   Play, stop, or update sound.    
.configure *option* *value*    
:   Toggle certain Dream Seeker config options, such as    
    `.configure graphics-hwmode on`. The only supported options you can    
    use are `graphics-hwmode`, `sound`, and `delay` which is an old    
    mechanism for dynamically adapting to network delay. (Usually the    
    `delay` is reset to 0.)    
.quit    
:   Closes Dream Seeker.    
### Embedded Winget    
Commands that are initiated by the skin (like button.command,    
map.on-show, etc.) have a special syntax that allows you to include    
information that would normally require a winget call. By including    
`[[`*`something`*`]]` in the command, the double-bracketed text will be    
replaced by the result of running a winget on that parameter.    
A value of `[[id.parameter]]` will run a winget on the control with the    
given ID. Just using `[[parameter]]` will run a winget for the control    
that initiated this command. You can also use `parent` in place of the    
ID to do something with the parent of the control, or `parent.id` for    
access to a sibling control. Position and size parameters can be further    
broken down by appending `.x` or `.y` to get at the numbers directly.    
Several commands already support some special cases like `[[*]]` or    
`[[width]]` or such, where the special-case values are relevant to the    
command. An example is that in `on-size` the value of `[[*]]` is a size    
value. The Any macro, gamepad macros, and mouse macros, also support    
this syntax; see [macros](/%7Bskin%7D/macros) for more info.    
You can choose how embedded wingets get formatted by following the value    
with `as` and a type, such as `[[window.size as string]]`. There are    
several types you can use, and different types of parameters get    
formatted differently:    
arg    
:   Value is formatted as if it\'s an argument on a command line.    
    Numbers are left alone; booleans are 0 or 1; size and position have    
    their X and Y values separated by a space; pretty much everything    
    else is DM-escaped and enclosed in quotes.    
escaped    
:   DM-escape the value as if it\'s in a quoted string but do not    
    include the quotes. Size and position values both use `,` to    
    separate their X and Y values.    
string    
:   Value is formatted as a DM-escaped string with surrounding quotes.    
params    
:   Format value for a URL-encoded parameter list (see    
    [list2params](/proc/list2params){.code}), escaping characters as    
    needed.    
json    
:   JSON formatting. Numbers are left unchanged; size or position values    
    are turned into objects with x and y items; boolean values are    
    `true` or `false`.    
json-dm    
:   JSON formatting, but DM-escaped so it can be included in a quoted    
    string. Quotes are not included.    
raw    
:   Does not change the value\'s text representation in any way; assumes    
    it\'s already formatted correctly for the purpose. This is similar    
    to `as arg` but does no escaping and no quotes.    
The `arg` type is the default, unless the `[[`*\...*`]]` expression has    
double quotes on both sides, in which case `escaped` is the default.  