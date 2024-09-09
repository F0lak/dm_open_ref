[]{#/proc/continue}    
## continue statement    
**See also:**    
:   [break statement](/ref/proc/break/break.md)    
:   [do proc](/ref/proc/do/do.md)    
:   [for loop proc](/ref/proc/for/loop/loop.md)    
:   [while proc](/ref/proc/while/while.md)    
<!-- -->    
**Format:**    
:   continue    
:   continue Label    
Begins the next iteration of the loop with the given label. If no label    
is specified, the innermost loop containing the continue statement is    
assumed.    
In a `for(Init,Test,Inc)` loop, the `continue` statement will jump to    
the `Inc` portion (if any) and move on to the conditional `Test`. In a    
`for(item in list)` loop, it will skip to the next item in the list. In    
a `while` or `do-while` loop, `continue` jumps to the condition in the    
`while` statement.    
### Example:    
client/verb/who() var/mob/M usr \<\< \"Players:\" for(M in world) if(M    
== usr) continue if(M.key) usr \<\< M.key    
This displays a list of players who have a mob in the world. The    
`continue` statement is used here to avoid including the user in the    
list. The same thing could have been achieved by using only the `if`    
statement. In more complicated situations, however, very long    
conditional expressions and deeply nested `if` statements can be avoided    
by using `continue` and its companion `break`.    
Here is an example using a label to continue an outer loop from inside    
an inner one: client/verb/loners() var/mob/M var/mob/G usr \<\<    
\"Loners:\" finding_loners: for(M in world) for(G in world) if(M in    
G.group) continue finding_loners //found a loner usr \<\< M.name    
This displays a list of mobs who do not belong in anyone else\'s group.    
Notice the syntax for labeling a list. The name of the block is simply    
placed in the code followed by a colon and its contents are indented    
inside it.  