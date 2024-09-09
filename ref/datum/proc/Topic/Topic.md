[]{#/datum/proc/Topic}    
## Topic proc (datum)    
**See also:**    
:   [Topic proc (client)](ref/client/proc/Topic)    
:   [ref text macro](ref/DM/text/macros/ref)    
<!-- -->    
**Format:**    
:   Topic(href,href_list\[\])    
<!-- -->    
**Args:**    
:   href: the hyperlink data (following ? in the URL).    
:   href_list: key/value list (from params2list(href)).    
This procedure is called by the default `client.Topic()` proc when the    
href contains a parameter called \"src\" containing an object reference.    
### Example:    
mob/verb/test() usr \<\< \"Click    
[here](?src=\ref%5Bsrc%5D;action=startgame)!\"    
mob/Topic(href,href_list\[\]) switch(href_list\[\"action\"\])    
if(\"startgame\") usr \<\< \"Starting game\...\"    
The above example uses an embedded reference to the player\'s own mob to    
create a hyperlink to that mob\'s `Topic()` proc. You can easily add    
different actions, parameters, and so forth. Just remember that the    
parameter values are always stored as text, so you need to convert those    
to whatever data format you need using procedures such as `text2num()`,    
`locate()`, etc.    
Always validate the input in `Topic()` calls to make sure it\'s correct    
and the query you\'re recieving is legitimate.  