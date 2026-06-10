
## xyz (var)

**Default Value:**
+   all 0
***
Set to different values to give your sound a 3D effect which will be applied when it is played. Positive values for `x` will sound as if they come from the right, positive `y` sounds like it is above the player's head, and positive `z` sounds like it is directly ahead. The effect of 3D sound depends on the player's computer's sound card, and is greatly enhanced when wearing headphones.

Depending on the value of `falloff`, the settings for the location of the sound can also affect its volume. Once the distance passes the value of `falloff`, the volume will diminish.

If these values are all set to 0, you should set `environment` if you want to treat it as a 3D sound. Otherwise BYOND will assume this is meant to be a non-3D sound such as music or the interface.

If the <a class="code" href="#/sound/var/atom">atom</a> var is set to an atom that's visible on the map (that is, if it's close enough to the center of view to be sent by the server), its relative x and y coordinates are fed through the <a class="code" href="#/sound/var/transform">transform</a> matrix, if present, and added to the x,y,z coordinates. This way, a sound's 3D position can change in real time. A sound is considered 3D if the `atom` var is set, even if the base x,y,z coordinates are all 0.
***
**Related Pages:**
+    [vars (sound)](/ref/sound/var)
+    [atom-linked](/ref/sound/var/atom)
+    [transform](/ref/sound/var/transform)
+    [falloff](/ref/sound/var/falloff)
