[]{#/operator/&&=}
  ## &&= operator {#operator byondver="514"}
  **See also:**
  :   [&& operator](ref/operator/&&)
  :   [\|\| operator](ref/operator/%7C%7C)
  :   [\|\|= operator](ref/operator/%7C%7C=)
  :   [operators](ref/operator)
  <!-- -->
  **Format:**
  :   A &&= B
  <!-- -->
  **Returns:**
  :   Value of `(A && B)` after it has been assigned to A. This expression
      can stand by itself; its result does not need to be assigned to
      anything else.
  First A is evaluated. If its value is true, B will be evaluated and
  assigned to A. If A is false, B will not be evaluated and A will remain
  unchanged.
  Note that this is slightly different from `if(A) A = B` if A is a
  complex expression such as `list[index++]`, because the expression is
  only evaluated once.
  This operator cannot be overloaded.