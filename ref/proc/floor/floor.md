[]{#/proc/floor}
  ## floor proc {#floor-proc byondver="515"}
  **See also:**
  :   [ceil proc](ref/proc/ceil)
  :   [round proc](ref/proc/round)
  :   [trunc proc](ref/proc/trunc)
  :   [fract proc](ref/proc/fract)
  <!-- -->
  **Format:**
  :   floor(A)
  <!-- -->
  **Returns:**
  :   the floor of A
  <!-- -->
  **Args:**
  :   A: A number, pixloc, or vector.
  Returns the floor of A (the largest integer less than or equal to A).
  ### Example:
  usr \<\< floor(1.45) // outputs 1 usr \<\< floor(-1.45) // outputs -2