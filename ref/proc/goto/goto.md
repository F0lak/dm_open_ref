[]{#/proc/goto}    
## goto proc    
**See also:**    
:   [break statement](/ref/proc/break/break.md)    
:   [continue statement](/ref/proc/continue/continue.md)    
:   [do proc](/ref/proc/do/do.md)    
:   [for loop proc](/ref/proc/for/loop/loop.md)    
:   [for list proc](/ref/proc/for/list/list.md)    
:   [while proc](/ref/proc/while/while.md)    
<!-- -->    
**Format:**    
:   goto node    
Jump to the specified node in the current proc.    
### Example:    
goto End world \<\< \"ERR\" End world \<\< \"The end\"    
This displays \"The end\".    
Note: `goto` should be used judiciously. It\'s easy to fall into the    
trap of \"spaghetti logic\" where `goto` is relied on so much that it    
becomes too difficult to follow how the flow of code execution will    
proceed. Normally, you\'ll want to use a construct like `while()` or    
`for()` loops, and `break` and `continue` statements. `goto` is for more    
complex situations that aren\'t readily handled by any of these.  