## .output (client command) 
###### BYOND Version 514
**See also:**
*   [output proc](/ref/proc/output.md) -m
*   [client commands](/ref/%7Bskin%7D/commands.md) -m
<!-- -->
**Format:**
*   .output *control* *text*


Sends output to a control. The text does not need quotes, but
any backslashes, newlines, and tabs should be escaped with a backslash.
This works similarly to the [`output()` proc](/ref/proc/output.md) -m. If text is
omitted, the control is cleared. 

Here is an example of using a
map control\'s [on-status](/ref/%7Bskin%7D/params/on-status.md) -m.code} event
to set a label rather than using the window\'s own statusbar.
    .output statuslabel [[* as escaped]]