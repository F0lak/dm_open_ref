
## atom (var)

**Default Value:**
+   null
***
Links this sound to an atom, whose position relative to the <a href="#/client/var/virtual_eye">vitual eye</a> (center of view), in tiles, is transformed and added to the 3D x,y,z coordinates. As you move relative to the atom, the sound's apparent position in 3D space will change without the server needing to update this sound manually.

This is usually used in conjunction with the <a class="code" href="#/sound/var/transform">transform</a> var, which converts the 2D x,y offset into 3D coordinates. This can scale or rotate the 2D coordinates however you need.

Note: The atom must remain "in range", meaning the server has to think it's close enough within visual range to send updates to the client, for the sound to be heard.
***
**Related Pages:**
+    [vars (sound)](/ref/sound/var)
+    [x, y, or z](/ref/sound/var/xyz)
+    [transform](/ref/sound/var/transform)
+    [falloff](/ref/sound/var/falloff)
