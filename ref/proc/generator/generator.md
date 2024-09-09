[]{#/proc/generator}
  ## generator proc {#generator-proc byondver="514"}
  **See also:**
  :   [Generators](ref/%7Bnotes%7D/generators)
  :   [Particle effects](ref/%7Bnotes%7D/particles)
  :   [color var (atom)](ref/atom/var/color)
  :   [Color matrix](ref/%7Bnotes%7D/color-matrix)
  :   [vector](ref/vector)
  :   [stddef.dm file](ref/%7B%7Bappendix%7D%7D/stddef%2edm)
  <!-- -->
  **Format:**
  :   generator(type, A, B, rand)
  <!-- -->
  **Args:**
  :   type: The type of generator object, which determines what kind of
      results it produces
  :   A: One extreme of the generator results
  :   B: The other extreme
  :   rand: Type of random distribution used
  Creates a generator that can be used to produce a random value. This
  generator can be used in client-side particle effects, or it can be used
  in proc code. The types of values it can produce are numbers, 2D or 3D
  vectors, or colors (a text string like \"#rrggbb\" or a color matrix).
    Generator type   Result type                      Description
    ---------------- -------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------
    num              num                              A random number between A and B.
    vector           vector                           A random vector on a line between A and B.
    box              vector                           A random vector within a box whose corners are at A and B.
    color            color (string) or color matrix   Result type depends on whether A or B are matrices or not. The result is interpolated between A and B; components are not randomized separately.
    circle           vector                           A random XY-only vector in a ring between radius A and B, centered at 0,0.
    sphere           vector                           A random vector in a spherical shell between radius A and B, centered at 0,0,0.
    square           vector                           A random XY-only vector between squares of sizes A and B. (The length of the square is between A\*2 and B\*2, centered at 0,0.)
    cube             vector                           A random vector between cubes of sizes A and B. (The length of the cube is between A\*2 and B\*2, centered at 0,0,0.)
  The optional `rand` argument determines the type of random distribution.
    -------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    UNIFORM_RAND   Default. Random values are uniformly likely to be chosen.
    NORMAL_RAND    Approximates a Gaussian normal distribution, but on a finite interval. Values closest to the mean are more likely to be chosen, while the extremes are much less likely.
    LINEAR_RAND    The probability of choosing a number is proportional to its absolute value.
    SQUARE_RAND    The probability of choosing a number is proportional to its square.
    -------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  The result of calling `generator()` is a datum of type `/generator` and
  you can get a random value from it by calling its `Rand()` proc.
  ### Example:
  var/generator/G = generator(\"num\", -1, 1) // generates a random number
  between -1 and 1 world \<\< G.Rand() // generate a number and output it
  to world
  Note: Worlds compiled in older BYOND versions before [vector](ref/vector)
  will return lists from vector generators.