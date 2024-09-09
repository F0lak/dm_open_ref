[]{#/proc/break}    
## break statement    
**See also:**    
:   [continue statement](/ref/proc/continue)    
:   [do proc](/ref/proc/do)    
:   [for loop proc](/ref/proc/for/loop)    
:   [while proc](/ref/proc/while)    
:   [switch proc](/ref/proc/switch)    
:   [#pragma syntax directive](/ref/DM/preprocessor/pragma/syntax)    
<!-- -->    
**Format:**    
:   break    
:   break Label    
Terminate the loop with the given label. If no label is specified, the    
innermost loop containing the `break` statement is assumed.    
### Example:    
obj/zapper verb/use() var/mob/M for(M in view()) if(!M.key) break if(!M)    
M = usr M \<\< \"ZAP!\" del(M)    
The zapper object kills the first mob it finds that doesn\'t belong to a    
player. If none can be found, it kills the user. Be careful! Note how    
this code takes advantage of the fact that the loop variable    
`M`{.variable} will be `null` if the loop terminates normally.    
For an example of how to use labeled loops, see the reference section    
for the `continue` statement.    
The `break` statement can also be used inside of a [`switch()`    
proc](/ref/proc/switch) when using [C-like    
syntax](/ref/DM/preprocessor/pragma/syntax), where it breaks out of a    
`case` block to the end of the switch. See [switch proc](/ref/proc/switch)    
for more details.  