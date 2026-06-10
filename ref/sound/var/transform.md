
## transform (var)

**Default Value:**
+   null (same as )
***
A 3x3 matrix for converting the 2D position of an atom, relative to the center of view, into 3D sound coordinates. (This value is meaningless if you don't link the sound to an atom via the <a href="#/sound/var/atom">atom</a> var.) The transformed vector is added to the sound's x,y,z values to get a 3D position.

The value of `transform` should be a list with 9 elements, in row-major order. The default list is `list(1,0,0, 0,1,0, 0,0,0)`. If you use a list shorter than 9 elements, the defaults will be filled in for you.

In easier-to-understand terms, this is how the result is calculated:


```dm

new_x = x * xx + y * yx + cx
new_y = x * xy + y * yy + cy
new_z = x * xz + y * yz + cz

```


It is helpful to think of each row in the matrix as what each component of the original vector will become. The first row of the matrix is the output x,y,z you'll get for an input x of 1.


```dm

obj/fire
    proc/HearMe(mob/player)
        var/sound/S = new('fire.ogg', channel=10, repeat=1)
        S.atom = src
        S.transform = list(1,0,0, 0,sqrt(0.5),sqrt(0.5), 0,0,0)
        player << S

```


The transform in this example rotates the fire's position by 45° forward, so positive y values get split between y and z. This gives the player the impression that an object higher up on their screen is both forward of and above them, as if they're looking down at the map from a 45° angle.
***
**Related Pages:**
+    [vars (sound)](/ref/sound/var)
+    [atom-linked](/ref/sound/var/atom)
+    [x, y, or z](/ref/sound/var/xyz)
+    [falloff](/ref/sound/var/falloff)
