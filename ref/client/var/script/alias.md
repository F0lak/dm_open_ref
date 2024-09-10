[]{#/aliases (client script).md}    
## aliases (client script)    
**See also:**    
:   [macros (client script)]/client/var/script/macro    
:   [script var (client)]/client/var/script    
:   [verbs]/verb    
Command aliases have a syntax similar to verbs. They define a command    
and a series of arguments which can then be used to execute a new    
command. The most common use for this is in a telnet world like a MUD.    
By defining aliases corresponding to the MUD commands, the player can    
have primitive command expansion and help.    
The syntax of an alias definition is best illustrated by the following    
example: alias/say(msg as text) set desc = \"speak your mind\" return    
\"say \[msg\]\"    
As you can see, it is just like a verb. Alias have all the same    
properties as verbs, except the `src` setting is always equal to the    
player.    
The value returned by an alias is executed as a command. In telnet mode,    
the command to execute is often simply the same as the command that was    
entered (since the alias was only defined to provide command expansion    
and help). Since that is such a common case, the return value defaults    
to the alias name followed by each of the arguments. The example above,    
for instance, would have the same effect without an explicit return    
statement.    
Note that commands executed via an alias are never interpreted as    
aliases. Otherwise, examples such as the one above would result in an    
infinite loop.  