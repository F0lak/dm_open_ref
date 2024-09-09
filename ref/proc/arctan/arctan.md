[]{#/proc/arctan}
  ## arctan proc {#arctan-proc byondver="513"}
  **See also:**
  :   [arcsin proc](ref/proc/arcsin)
  :   [arccos proc](ref/proc/arccos)
  :   [tan proc](ref/proc/tan)
  :   [turn proc](ref/proc/turn)
  <!-- -->
  **Format:**
  :   arctan(Num)
  :   arctan(x, y)
  :   arctan(Vector)
  <!-- -->
  **Args:**
  :   Num: A number
  :   x, y: 2D coordinates
  :   Vector: A vector (only 2 dimensions are used)
  <!-- -->
  **Returns:**
  :   The inverse tangent in degrees.
  When `arctan` is called with just one number argument, the number is a
  tangent, and the return value is the angle that produces that tangent.
  The resulting angle can range from -90 to 90.
  The two-argument form returns a polar angle from -180 to 180. This angle
  starts at 0° for due east, and increases counter-clockwise from there.
  Therefore 1,0 has an arctangent of 0°, 0,1 is 90°, -1,0 is 180°, and so
  on. At point 0,0 the angle is undefined since it could be any angle, but
  `arctan` will return 0.
  Finally, you can use a vector instead of a number. Only the x and y
  components of a vector will be used.
  ### Example:
  mob/verb/test() usr \<\< arctan(0) // 0 usr \<\< arctan(1) // 45 usr
  \<\< arctan(sqrt(3)) // 60 // polar coordinates usr \<\< arctan(3, 4) //
  53.1301 usr \<\< arctan(-1, 1) // 135 usr \<\< arctan(0, -5) // -90
  Here\'s another example, in which a rotating turret points to a target
  on another tile. mob/turret proc/PointAt(atom/target) if(!target) return
  var/dx = target.x - x var/dy = target.y - y // turret\'s icon normally
  faces east transform = matrix().Turn(-arctan(dx, dy))