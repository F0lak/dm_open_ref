## initial proc
**See also:**
*   [:* operator](/ref/operator/::.md) 
*   [issaved proc](/ref/proc/issaved.md) 
*   [vars list var (datum)](/ref/datum/var/vars.md) <!-- -->
**Format:**
*   initial(Var)
<!-- -->
**Args:**
*   Var* A variable to find the initial value of.


This returns the original compile-time value of a variable. It
could be used to reset a variable to its default value or to check if a
variable has changed.
### Example:

```
 obj/verb/set_icon(I as null\|icon) if(!I) I = initial(icon)
icon = I 
```
 This example allows an object\'s icon to be
modified. If the user does not specify a new icon, it will be reset to
the original one.