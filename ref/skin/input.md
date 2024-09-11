## input control (skin)


A text box into which the user can type. By default this is
used for sending [client commands](/%7Bskin%7D/commands), but it can be
used for other purposes as well.
**Input-specific parameters:**
*   [command](/%7Bskin%7D/param/command)
*   [is-password](/%7Bskin%7D/param/is-password)
*   [multi-line](/%7Bskin%7D/param/multi-line)
*   [no-command](/%7Bskin%7D/param/no-command)
*   [on-blur](/%7Bskin%7D/param/on-blur)
*   [on-focus](/%7Bskin%7D/param/on-focus)
*   [text](/%7Bskin%7D/param/text)


Note that when in \"standard\" mode of accepting user commands,
built-in verbs like `.click`, or local commands like `.winset`, are not
accepted when typed in. This kind of command can still be entered
manually through the Client menu of the Options & Messages window.