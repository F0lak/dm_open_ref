
## matrix (info)
***
To display rotation, scaling, and other transformations on atoms, DM uses 2D matrices. The /matrix datum is a convenient way of handling the numbers involved, as it can be easily manipulated. There are six vars, a through f, laid out like so:

When an x,y point is multiplied by the matrix, it becomes the new point x',y'. This is equivalent to:

The default matrix is:

Matrices are created with the matrix() proc, or by calling new/matrix(). (See the matrix() proc for examples.) They are also created as needed whenever you read from atom.transform or use certain operators.

Manipulation of matrices can be done with operators, or with procs. You can do the following with them:

When you've built your matrix, you can assign it to atom.transform to change the way that atom is displayed.

The matrices supported by this datum are **not** the same kind used to transform colors, as in the atom.color var and icon.MapColors() proc. For color matrices, see <a href="#/{notes}/color-matrix">color matrix</a>.
***
**Related Pages:**
+    [New](/ref/proc/matrix)
+    [matrix operators](/ref/matrix/operators)
+    [matrix procs](/ref/matrix/proc)
+    [transform var (atom)](/ref/atom/var/transform)
+    [stddef.dm file](/ref/{{appendix}}/stddef%2edm)
