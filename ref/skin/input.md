## input control (skin)


A text box into which the user can type. By default this is
used for sending [client commands](/ref/%7Bskin%7D/commands.md) , but it can be
used for other purposes as well.
**Input-specific parameters:**
*   [command](/ref/%7Bskin%7D/param/command.md) 
*   [is-password](/ref/%7Bskin%7D/param/is-password.md) 
*   [multi-line](/ref/%7Bskin%7D/param/multi-line.md) 
*   [no-command](/ref/%7Bskin%7D/param/no-command.md) 
*   [on-blur](/ref/%7Bskin%7D/param/on-blur.md) 
*   [on-focus](/ref/%7Bskin%7D/param/on-focus.md) 
*   [text](/ref/%7Bskin%7D/param/text.md) 

Note that when in \"standard\" mode of accepting user commands,
built-in verbs like `.click`, or local commands like `.winset`, are not
accepted when typed in. This kind of command can still be entered
manually through the Client menu of the Options & Messages window.