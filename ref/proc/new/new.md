[]{#/proc/new}
  ## new proc
  **See also:**
  :   [New proc (atom)](ref/atom/proc/New)
  :   [New proc (datum)](ref/datum/proc/New)
  :   [New proc (icon)](ref/icon/proc/New)
  :   [newlist proc](ref/proc/newlist)
  :   [path operators](ref/operator/path)
  :   [\_\_IMPLIED_TYPE\_\_ macro](ref/DM/preprocessor/__IMPLIED_TYPE__)
  <!-- -->
  **Format:**
  :   new Type(Args)
  <!-- -->
  **Returns:**
  :   A reference to a new instance of Type.
  <!-- -->
  **Args:**
  :   Type: The type of object to create.
  :   Args: Arguments for the Type.New() proc.
  A new instance of Type is created. The arguments (Args) are passed to
  its New() proc. A handy short-cut: if Type is not specified and new() is
  being used in an assignment, the variable type of the left-hand-side
  will be used as the default type.
  The atom types /area, /turf, /obj, and /mob all take a location argument
  specifying the initial position. If not specified, it defaults to null.
  Newly created areas or turfs replace any existing area or turf at the
  specified location.
  ### Example:
  obj/stick mob/verb/magic_stick() var/obj/stick/S = new(src) //create a
  stick in my inventory S.desc = \"This is no ordinary stick!\" view()
  \<\< \"\[src\] creates \\an \[S\] from thin air!\"