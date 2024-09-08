[]{#/world/var/loop_checks}
## loop_checks var (world)
**Default value:**
:   1
Setting this to 0 disables the very long loop protection. By default,
loops in the code which undergo a very large number of iterations or
recursions are aborted (by crashing the proc). This prevents the proc
from locking up the server for too long.
You may need to disable this feature if your code has some very long
loops in it. Before doing that, make sure it\'s not *infinitely* long!
Your program will utterly crash if it runs out of system stack space,
which can happen in a very deep or infinite recursion.
Note: The compiler will now generate a warning when you disable
`loop_checks`. It is not advisable to disable the check unless you\'re
trying to debug something, since you can cause the server to hang.
Generally if you have a loop so long it can cause the regular loop
checks to freak out, you need to make a change to the loop behavior
anyway.