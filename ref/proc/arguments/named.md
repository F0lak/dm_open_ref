## named arguments (proc)
**See also:**
*   [New proc (atom)](/ref/atom/proc/New.md) 
*   [arglist proc](/ref/proc/arglist.md) 
*   [arguments (proc)](/ref/proc/arguments.md) 

The parameters passed to a procedure are called arguments.
These may either be passed in positional order, or they can be passed as
*named arguments*. Not all procedures are defined with the intention of
supporting named arguments, so consult the documentation for the
procedure in question first. (This is mainly an issue of whether the
argument names might change in the future.) 

The following
example shows several ways of producing the same call to a procedure.
### Example:

```
 mob/proc/MyProc(a,b,c) src \<\< \"MyProc(\[a\],\[b\],\[c\])\"
mob/verb/test() MyProc(1,2,3) //positional parameters
MyProc(a=1,b=2,c=3) //named arguments MyProc(1,b=2,c=3) //positional and
named arguments MyProc(c=3,a=1,b=2) //named arguments can come in any
order 
```
 

To prevent silent errors, named arguments that
do not match any of the arguments of the procedure being called will
generate a runtime error. This is somewhat different from the behavior
of positional arguments in DM where it is perfectly acceptable to pass
more arguments than were explicitly defined in the procedure.


As always, arguments that are not assigned in the call will
simply be given the value null (or whatever default value is specified
in the definition). 

When an object procedure is overridden, the
variable names in the new definition are the ones that get matched
against named arguments in a call to that procedure. A procedure which
is intended to support named arguments should therefore be defined with
care so as to conform to the interface expected by users of the
procedure. That doesn\'t stop you from changing that interface when
overriding a procedure, but the normal case would be to preserve the
argument names of the base procedure when overriding it. 

The
following example is not useful, but it illustrates a situation where a
procedure is overridden so as to preserve the same argument names and
positions. As mentioned above, you are not *required* to preserve either
the names or positions, but that is usually what you want.
### Example:

```
 mob proc/MyProc(a,b,c) usr \<\<
\"mob.MyProc(\[a\],\[b\],\[c\])\" mob/verb/test() MyProc(a=1,b=2,c=3)
special_mob MyProc(a,b,c,d) if(d) ..() //pass in same order else
..(c,b,a) //pass in reverse order test() MyProc(a=1,b=2,c=3,d=0)
//normal order MyProc(a=1,b=2,c=3,d=1) //reverse the order 
```



This example merely used positional parameters in the call to
`..()`, but one can use named arguments there too if it is desirable.


The best time to use named arguments is when calling a
procedure that takes a lot of optional parameters. You can just name the
ones that you want to assign and leave the rest unspecified. Trying to
do the same thing with positional parameters can be much more
awkward--especially when the arguments you do want to assign are
preceded by a number of ones that you don\'t care to assign. It\'s easy
to lose your place in the list or to forget what it does. 

Since
named arguments involve a slight amount of extra overhead, one should
avoid them in code that is highly cpu intensive due to being called many
many times. Otherwise, code clarity may be a bigger priority.