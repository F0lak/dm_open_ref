## SendPage proc (client)
**Format:**
*   SendPage(msg,recipient,options)
<!-- -->
**Returns:**
*   Returns number of recipients successfully contacted.
<!-- -->
**Args:**
*   msg* text to send
*   recipient* key or list of keys to page
*   options* text string containing key=value options


The user is prompted to authorize sending of the pager message.
The recipient may easily respond or jump to the sender\'s location by
clicking on the link in the pager message. The effect is identical to
that of the sending a page through the Dream Seeker pager. 

The
options are encoded in the same format read by text2params(). The valid
options are:
summon (0/1)
*   If not included in the options, this is 0. If included in the
    options without assigning it to anything, it is 1. A value of 1
    sends the recipient the sender\'s location so they can join by
    clicking on the message.
email (0/1)
*   If not included in the options, this is 0. If included in the
    options without assigning it to anything, it is 1. A value of 1
    sends causes the message to be delivered as email. If this is not
    possible, it is delivered as a long-lived pager message. Normally,
    pager messages expire within a short time after being sent (half an
    hour).
subject
*   For email messages, this specifies the subject to use.