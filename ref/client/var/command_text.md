## command_text (client) 
###### BYOND Version d_text (client) {#command_text-client deprecated="1

<!-- -->
**Default value:**
+   null
Note: In BYOND 4.0 this var is deprecated. The
[command](/ref/%7Bskin%7D/param/command.md) {.code} parameter for an [Input
control](/ref/%7Bskin%7D/control/input.md)  can be set to `!command` (`!` in
front of your default command) which does the same thing. 

This
text is placed onto the command line, to be followed by whatever the
user may type. It is usually the name of a verb followed by a space,
such as `"say "`. The user can clear this and enter a different command
by hitting backspace, escape, delete, or `/`.
### Example:

```
 client command_text = \"say \" verb/say(T as text) world \<\<
\"\[usr\] says, \'\[T\]\'\" 
```
 

It is also possible to
turn on macro mode, in which each keypress executes a [keyboard
macro](/ref/client/var/script/macro.md)  by setting `command_text` to
`".alt "`. That stands for the *Alt* key, which can be used to execute
macros in normal mode. 

This variable could also be used to
create a specialized command prompt. For example, a traditional style
MUD command-line could be implemented like this:
### Example:

```
 client command_text = \"\> \" verb/command(C as command_text)
set name = \"\>\" usr \<\< \"Your command: \[C\]\" 
```



This example uses the `command_text` input type, which accepts
raw text, with no quoting, escaping, or translating, so that you can
invent whatever syntax you want.

**See also:**
+   [arguments (verb)](/ref/verb/arguments.md) 
+   [command parameter](/ref/%7Bskin%7D/param/command.md) 
+   [macros (client script)](/ref/client/var/script/macro.md) 
+   [Input control (skin)](/ref/%7Bskin%7D/control/input.md) 
+   [command parameter (skin)](/ref/%7Bskin%7D/param/command.md) 
+   [macros (skin)](/ref/%7Bskin%7D/macros.md) 