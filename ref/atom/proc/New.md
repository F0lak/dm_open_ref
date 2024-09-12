## New proc (atom)
**See also:**
+   [New proc (datum)](/ref/datum/proc/New.md) 
+   [new proc](/ref/proc/new.md) 
<!-- -->
**Format:**
+   New(loc)
+   [(supports [named arguments](/ref/proc/arguments/named.md) ]{.small}
<!-- -->
**When:**
+   Called when the object is created.
<!-- -->
**Args:**
+   loc: The initial location.
<!-- -->
**Default action:**
+   None.


By the time New() is called, the object has already been
created at the specified location and all of its variables have been
initialized. You can perform additional initialization by overriding
this procedure. 

Since the initial location parameter passed to
`new()` is applied before New() is even called, there is some special
handling of the `loc`{.variable} variable when using named arguments in
a call. Normally, if a procedure is overridden, named arguments in a
call are matched against those in the the overridden definition. In this
case, however, the `loc`{.variable} parameter name is hard-coded.
Regardless of what you call the first argument in your definition of
New(), the initial location will be taken from the first positional
argument, or from the argument named `loc`{.variable} if there are no
positional arguments. 

The following example does some extra
initialization that is not possible in the variable definition section,
because it requires a runtime evaluation. This is a common reason to use
New().
### Example:

```
 mob var birthdate //time stamp New() birthdate =
world.realtime return ..() verb/look() set src in view() usr \<\<
\"\[src\] was born on \[time2text(birthdate,\"DD-MMM-YYYY\")\].\"

```
