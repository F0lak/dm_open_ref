## script var (client)

    script)](/ref/client/var/script/PASSWORD_TRIGGER.md) 
+   [URL (client script)](/ref/client/var/script/URL.md) 
+   [aliases (client script)](/ref/client/var/script/alias.md) 
+   [browser configuration](/ref/client/var/script/URL/browser.md) 
+   [command_text (client)](/ref/client/var/command_text.md) 
+   [macros (client script)](/ref/client/var/script/macro.md) 
+   [macros (skin)](/ref/skin/macros.md) 
+   [style sheets](/ref/DM/text/style.md) 
+   [style sheets (in scripts)](/ref/client/var/script/style.md) <!-- -->
**Default value:**
+   none


Client scripts are mini-programs used to configure the client.
The language they use is called DM Script, and will undoubtedly expand
in the future. Currently, client scripts can be used to define style
sheets, command aliases, and macros. When executed directly by a player,
they can also be used to specify an initial URL to open and a password
trigger (for some ancient telnet worlds that don\'t suppress password
echo). 

For the specific syntax of DM Script, see the relevant
reference sections listed above. 

The `client.script` variable
may be assigned to script code in a text string (double quotes) or in a
file (single quotes). You can also simply include the file in your
project or explicitly use the `#include` statement. Files containing DM
Script should have the extension `.dms`. 


### Example:

``` dm
 client/script = "
" 
```
 

This example selects a default monospace font for
all output to the terminal. 

In addition to scripts loaded via
`client.script`, the player may have *client-side* scripts. These are
either called *connection* scripts or *post-connection* scripts
depending on whether they are used to automatically connect to a world
or whether they are executed automatically after connecting to a world.
In either case, the player\'s scripts are always executed before the
designer\'s `client.script` script, so style sheets from the designer
have higher precedence by default. 

There are three
post-connection client-side scripts for the three types of worlds the
client can connect to: `byond.dms`, `telnet.dms`, and `irc.dms`. These
are automatically executed if the player connects directly to a world
without using a connection script to do so. The intention is to load any
standard configurations such as style sheets and command aliases.

> [!TIP] 
> **See also:**
> +   [#include directive](/ref/DM/preprocessor/include.md) 
> +   [PASSWORD_TRIGGER (client