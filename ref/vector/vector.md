[]{#/vector}
  ## vector {#vector byondver="516"}
  **See also:**
  :   [vector proc](ref/proc/vector)
  :   [procs (vector)](ref/vector/proc)
  :   [vars (vector)](ref/vector/var)
  :   [pixloc](ref/pixloc)
  :   [operators](ref/operator)
  :   [matrix](ref/matrix)
  A primitive value representing a numeric vector in 2 or 3 dimensions.
  That is, a 2D vector has x and y components, and a 3D vector has x, y,
  and z components.
  Vectors are primarily useful for physics and distance calculations.
  Vectors can be treated as a list for purposes of using the indexing `[]`
  operator, or a for loop. The `len` var is the number of components in
  the list, just like a regular list.
  Vectors support most math operations. Multiplication and division can be
  done with either a single number or a vector; the latter will act
  piecewise on each component, just like addition and subtraction do.
  When doing math on two vectors of different dimensions, the result will
  use the highest dimensionality. E.g., adding a 2D and 3D vector produces
  a 3D vector.
  Other supported procs for vectors include:
  [min()](ref/proc/min){.code}
  [max()](ref/proc/max){.code}
  [clamp()](ref/proc/clamp){.code}
  [round()](ref/proc/round){.code}
  [floor()](ref/proc/floor){.code}
  [ceil()](ref/proc/ceil){.code}
  [trunc()](ref/proc/trunc){.code}
  [fract()](ref/proc/fract){.code}