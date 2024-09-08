[]{#/var/global}
## global vars
**See also:**
:   [vars](#/var)
The global type modifier makes a var permanent and shared. This means
only one copy of the var is maintained. Otherwise, separate copies of
the var are maintained for each instance containing the var (be it a
proc, mob, obj, etc.)
### Example:
mob/proc/Counter() var/global/count src \<\< \"Count = \[++count\]\"
This example increases the count each time the proc is called. If count
were not declared global, the displayed count would be 1 every time.