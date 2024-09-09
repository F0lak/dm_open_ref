[]{#/client/var/inactivity}
  ## inactivity var (client)
  **See also:**
  :   [tick_lag var (world)](ref/world/var/tick_lag)
  This is equal to the amount of time (in server ticks, which default to
  1/10s) since the player\'s last action (such as executing a verb,
  moving, clicking an object, or selecting a topic link). This value is
  reset to 0 after each new action so you can use it to determine the time
  that has passed since the last one.
  ### Example:
  mob/verb/inactivity() usr \<\< \"You have been inactive for
  \[client.inactivity/10\] seconds.\"