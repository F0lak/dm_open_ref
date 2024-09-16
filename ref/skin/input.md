## input control (skin)


A text box into which the user can type. By default this is
used for sending [client commands](/ref/skin/commands.md) , but it can be
used for other purposes as well.
**Input-specific parameters:**
+   [command](/ref/skin/param/command.md) 
+   [is-password](/ref/skin/param/is-password.md) 
+   [multi-line](/ref/skin/param/multi-line.md) 
+   [no-command](/ref/skin/param/no-command.md) 
+   [on-blur](/ref/skin/param/on-blur.md) 
+   [on-focus](/ref/skin/param/on-focus.md) 
+   [text](/ref/skin/param/text.md) 

Note that when in \"standard\" mode of accepting user commands,
built-in verbs like `.click`, or local commands like `.winset`, are not
accepted when typed in. This kind of command can still be entered
manually through the Client menu of the Options & Messages window.