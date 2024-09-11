## macros (client script)
**See also:**
*   [macros (skin)](/%7Bskin%7D/macros)
*   [aliases (client script)](/client/var/script/alias)
*   [command_text (client)](/client/var/command_text)
*   [script var (client)](/client/var/script)
*   [verbs](/verb)


Macros are just like aliases, except that they are triggered by
a single key (or combination of keys) instead of a full command. When a
macro is executed, it returns a text string which is then executed as a
command. So a macro is just a short-cut for entering a command.


The following example illustrates the syntax for entering a
typical set of macros.
### Example;

```
 macro ALT+I return \"inventory\" ALT+SHIFT+I return
\"inventory\\nequipment\" //multiple commands ALT+s return \"say
\\\...\" //command to be edited 
```

Note* In old versions of BYOND, character keys required the Alt key to
be pressed to trigger the macro, and did not include `"ALT+"` to do so.
This behavior has changed, and the name of the macro is just like the
format used in skin files. You can now use a key name, and modifiers
like `SHIFT+`, `CTRL+`, `ALT+`, `+REP`, and `+UP`. Old .dms and
[`client.script`](/client/var/script) files (prior to version 507)
should be updated accordingly when recompiling in a newer version.