[]{#/icon/proc/Turn}
  ## Turn proc (icon)
  **See also:**
  :   [Flip proc (icon)](ref/icon/proc/Flip)
  :   [dir var (atom)](ref/atom/var/dir)
  :   [icon](ref/icon)
  :   [procs (icon)](ref/icon/proc)
  <!-- -->
  **Format:**
  :   Turn(angle)
  <!-- -->
  **Args:**
  :   angle: an angle in degrees
  This rotates the icon clockwise by the specified amount.
  ### Example:
  mob/verb/drink() //this effect is very confusing! var/icon/I =
  new(usr.icon) I.Turn(90) usr.icon = I usr \<\< \"You feel a little
  tipsy!\" sleep(200) I.Turn(-90) //turn it back usr.icon = I //should
  have just saved original value
  If an icon is not square, it cannot be turned.