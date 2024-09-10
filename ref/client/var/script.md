[]{#/script var (client).md}    
## script var (client)    
**See also:**    
:   [#include directive]/DM/preprocessor/include    
:   [PASSWORD_TRIGGER (client    
    script)]/script var (client.md/PASSWORD_TRIGGER)    
:   [URL (client script)]/script var (client.md/URL)    
:   [aliases (client script)]/script var (client.md/alias)    
:   [browser configuration]/script var (client.md/URL/browser)    
:   [command_text (client)]/client/var/command_text    
:   [macros (client script)]/script var (client.md/macro)    
:   [macros (skin)]/%7Bskin%7D/macros    
:   [style sheets]/DM/text/style    
:   [style sheets (in scripts)]/script var (client.md/style)    
<!-- -->    
**Default value:**    
:   none    
Client scripts are mini-programs used to configure the client. The    
language they use is called DM Script, and will undoubtedly expand in    
the future. Currently, client scripts can be used to define style    
sheets, command aliases, and macros. When executed directly by a player,    
they can also be used to specify an initial URL to open and a password    
trigger (for some ancient telnet worlds that don\'t suppress password    
echo).    
For the specific syntax of DM Script, see the relevant reference    
sections listed above.    
The `client.script` variable may be assigned to script code in a text    
string (double quotes) or in a file (single quotes). You can also simply    
include the file in your project or explicitly use the `#include`    
statement. Files containing DM Script should have the extension `.dms`.    
### Example:    
client/script = \"    
\"    
This example selects a default monospace font for all output to the    
terminal.    
In addition to scripts loaded via `client.script`, the player may have    
*client-side* scripts. These are either called *connection* scripts or    
*post-connection* scripts depending on whether they are used to    
automatically connect to a world or whether they are executed    
automatically after connecting to a world. In either case, the player\'s    
scripts are always executed before the designer\'s `client.script`    
script, so style sheets from the designer have higher precedence by    
default.    
There are three post-connection client-side scripts for the three types    
of worlds the client can connect to: `byond.dms`, `telnet.dms`, and    
`irc.dms`. These are automatically executed if the player connects    
directly to a world without using a connection script to do so. The    
intention is to load any standard configurations such as style sheets    
and command aliases.  