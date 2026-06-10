
## SendPage (proc)

**Format:**
+   SendPage(msg,recipient,options)

**Arguments:**
+   msg: text to send
+   recipient: key or list of keys to page
+   options: text string containing key=value options

**Returns:**
+   Returns number of recipients successfully contacted.
***
The user is prompted to authorize sending of the pager message. The recipient may easily respond or jump to the sender's location by clicking on the link in the pager message. The effect is identical to that of the sending a page through the Dream Seeker pager.

The options are encoded in the same format read by text2params(). The valid options are:
***