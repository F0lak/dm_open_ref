## goto proc
**See also:**
*   [break statement](/proc/break)
*   [continue statement](/proc/continue)
*   [do proc](/proc/do)
*   [for loop proc](/proc/for/loop)
*   [for list proc](/proc/for/list)
*   [while proc](/proc/while)
<!-- -->
**Format:**
*   goto node


Jump to the specified node in the current proc.
### Example:

```
 goto End world \<\< \"ERR\" End world \<\< \"The end\"

```
 

This displays \"The end\". 

Note* `goto`
should be used judiciously. It\'s easy to fall into the trap of
\"spaghetti logic\" where `goto` is relied on so much that it becomes
too difficult to follow how the flow of code execution will proceed.
Normally, you\'ll want to use a construct like `while()` or `for()`
loops, and `break` and `continue` statements. `goto` is for more complex
situations that aren\'t readily handled by any of these.