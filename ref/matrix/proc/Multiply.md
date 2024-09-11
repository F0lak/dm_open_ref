## Multiply proc (matrix)
**See also:**
*   [matrix](/matrix)
*   [matrix operators](/matrix/operators)
*   [matrix procs](/matrix/proc)
*   [\*= operator](/operator/*)
<!-- -->
**Format:**
*   Multiply(Matrix2)\
    *or*
*   Multiply(n)
<!-- -->
**Args:**
*   Matrix2* another matrix
*   n* a number
<!-- -->
**Returns:**
*   src


This multiplies the current matrix by Matrix2 or n. If the n
format is used, this is just like scaling the whole matrix. If another
matrix is multiplied, then it is like doing the two transformations in
order* src, then Matrix2. 

Multiplication of one matrix by
another depends on the order. You may get a different result multiplying
A \* B vs. B \* A.