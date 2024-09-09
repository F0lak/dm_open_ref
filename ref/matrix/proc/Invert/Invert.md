[]{#/matrix/proc/Invert}
  ## Invert proc (matrix)
  **See also:**
  :   [matrix](ref/matrix)
  :   [matrix operators](ref/matrix/operators)
  :   [matrix procs](ref/matrix/proc)
  :   [\~ operator](ref/operator/~)
  <!-- -->
  **Format:**
  :   Invert()
  <!-- -->
  **Returns:**
  :   src
  This inverts the current matrix, if possible.
  Not all matrices can be inverted. If it\'s not possible, the matrix is
  said to be degenerate. This happens if, for example, all of the values
  in the matrix are zero. A degenerate matrix will not be changed by this
  proc.