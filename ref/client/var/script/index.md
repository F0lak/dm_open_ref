
## script (var)

**Default Value:**
+   none
***
Client scripts are mini-programs used to configure the client. The language they use is called DM Script, and will undoubtedly expand in the future. Currently, client scripts can be used to define style sheets, command aliases, and macros. When executed directly by a player, they can also be used to specify an initial URL to open and a password trigger (for some ancient telnet worlds that don't suppress password echo).

For the specific syntax of DM Script, see the relevant reference sections listed above.

The <code>client.script</code> variable may be assigned to script code in a text string (double quotes) or in a file (single quotes). You can also simply include the file in your project or explicitly use the <code>#include</code> statement. Files containing DM Script should have the extension <code>.dms</code>.


```dm

client/script = ""

```


This example selects a default monospace font for all output to the terminal.

In addition to scripts loaded via <code>client.script</code>, the player may have <em>client-side</em> scripts. These are either called <em>connection</em> scripts or <em>post-connection</em> scripts depending on whether they are used to automatically connect to a world or whether they are executed automatically after connecting to a world. In either case, the player's scripts are always executed before the designer's <code>client.script</code> script, so style sheets from the designer have higher precedence by default.

There are three post-connection client-side scripts for the three types of worlds the client can connect to: <code>byond.dms</code>, <code>telnet.dms</code>, and <code>irc.dms</code>. These are automatically executed if the player connects directly to a world without using a connection script to do so. The intention is to load any standard configurations such as style sheets and command aliases.
***
**Related Pages:**
+    [#include directive](/ref/DM/preprocessor/include)
+    [PASSWORD_TRIGGER (client script)](/ref/client/var/script/PASSWORD_TRIGGER)
+    [URL (client script)](/ref/client/var/script/URL)
+    [aliases (client script)](/ref/client/var/script/alias)
+    [browser configuration](/ref/client/var/script/URL/browser)
+    [command_text (client)](/ref/client/var/command_text)
+    [macros (client script)](/ref/client/var/script/macro)
+    [macros (skin)](/ref/{skin}/macros)
+    [style sheets](/ref/DM/text/style)
+    [style sheets (in scripts)](/ref/client/var/script/style)
