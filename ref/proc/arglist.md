## arglist proc
**See also:**
*   [arguments (proc)](/proc/arguments)
*   [call proc](/proc/call)
*   [call_ext proc](/proc/call_ext)
*   [list proc](/proc/list)
<!-- -->
**Format:**
*   arglist(List)
<!-- -->
**Args:**
*   List* a list to be used as the arguments to a procedure


Normally, if you were to pass a list directly to a procedure,
it would only come through as a singe argument to that procedure. In
some cases, you might instead want the items in the list to become the
arguments to the procedure. That is what `arglist()` achieves.


If the items in the list are associations, these are treated as
[named arguments](/proc/arguments/named). Each such list item is
matched against the names of the procedure arguments and its associated
value is assigned to that parameter. 

Most built-in DM
instructions do not support use of `arglist()`, but all user-defined
procedures automatically support it. The built-in instructions which
support named arguments will also support `arglist()`. 

The
following example shows how to use `arglist()` with both positional
parameters and named arguments. Both of these examples could be replaced
by a much simpler direct call without need for a list to hold the
arguments; this is just to illustrate the syntax.
### Example:

```
 proc/MyProc(a,b) usr \<\< \"MyProc(\[a\],\[b\])\"
mob/verb/test() var/lst = list(1,2) MyProc(arglist(lst)) //MyProc(1,2)
lst = list(b=2,a=1) //just to illustrate that order does not matter
MyProc(arglist(lst)) //MyProc(b=2,a=1) \--\> MyProc(1,2) 
```
