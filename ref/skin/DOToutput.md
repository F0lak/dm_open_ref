[]{#/DOToutput (client command).md}/commands/.output}    
## .output (client command) {#output-client-command byondver="514"}    
**See also:**    
:   [output proc]/proc/output    
:   [client commands]/%7Bskin%7D/commands    
<!-- -->    
**Format:**    
:   .output *control* *text*    
Sends output to a control. The text does not need quotes, but any    
backslashes, newlines, and tabs should be escaped with a backslash. This    
works similarly to the [`output()` proc]/proc/output. If text is    
omitted, the control is cleared.    
Here is an example of using a map control\'s    
[on-status]/%7Bskin%7D/params/on-status{.code} event to set a label    
rather than using the window\'s own statusbar.    
    .output statuslabel [[* as escaped]]  