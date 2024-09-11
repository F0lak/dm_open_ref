## sleep_offline var (world)
**Default value:**
*   0


Setting this to 1 causes the world to be suspended when there
are no players, even if you have sleeping procs waiting to happen. The
default value is 0, which means the server will only sleep if there are
no players and no procs waiting to happen. The main purpose of the
variable is to save the cpu from doing work when there is nobody around
to appreciate it. On the other hand, that doesn\'t give the poor NPC\'s
a break from the nasty humans.