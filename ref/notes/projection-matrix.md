
## projection-matrix (info)
***
Note: Currently this feature applies only to particle effects, using the `transform` var.

Normally icons in BYOND can only be transformed in 2D, using a simple 3x3 matrix. This is represented by the `/matrix` object, which cuts off the last column because it isn't used. However particles can have coordinates in x, y, and z, and the whole particle set can be given a transformation matrix that handles all three dimensions.

The easiest transformation for particles is a simple 2D one, which you can do by setting the particle datum's `transform` var to a `/matrix` object.

When an x,y point is multiplied by the matrix, it becomes the new point x',y'. This is equivalent to:

This is called an **affine transform** because all the operations are "linear" in math terms. (That is, every term in the formula above has a single variable, not raised to a higher power than 1.)

3D affine transforms of this type are also affine transformations. There is no special object for this so a list is used (see below).

The way to read the vars above is that the first letter says what input component is being transformed (x,y,z, or c for "constant"), and the second letter is the output component.

To use this kind of matrix, you can cut off the 4th column and provide the values in a list form, in row-major order:


```dm
list(xx,xy,xz, yx,yy,yz, zx,zy,zz, cx,cy,cz)
```


Note the 4th row is also optional.

This is the most interesting matrix, since if you use all 4 columns you're actually altering an "axis" called w. This isn't a real axis, but is just a number that the resulting vector will be divided by.

In a regular affine transform, w always stays at 1. In projection you can think of w as a distance from the "camera". 1 is where objects are their "normal" size. If you make the z value affect w' by setting zw, you basically make an object look smaller at higher z values.

This is a simple projection matrix where x,y,z are left untouched, but there's a projection effect. The "D" value is how far away the "camera" is from z=0, so a point at z=D looks like it's twice as far away.

This 4x4 matrix is handled as a list just like the 3x4 affine matrix:


```dm
list(xx,xy,xz,xw, yx,yy,yz,yw, zx,zy,zz,zw, wx,wy,wz,ww)
```

***