
## eye (var)

**Default Value:**
+   The connected mob, client.mob.
***
This value determines the center of the player's map. The default value simply means that the visible region is normally centered on the player's mob. Effects such as setting <code>perspective</code> to <code>EDGE_PERSPECTIVE</code> or using <code>lazy_eye</code> can move the map off-center temporarily. The eye is the *ideal* center, not necessarily the actual center; to find the actual center, use <code>virtual_eye</code>.

The eye's step_x/y vars, if present, are also used to allow smooth scrolling of the map. These also obey lazy_eye and edge_limit.

Note that the visibility of objects is still computed from the point of view of the mob rather than the eye. This allows the use of <code>lazy_eye</code> or similar effects that control the panning of the map while still having the player see only what the mob can see. To determine visibility from the eye, you can change the value of <code>client.perspective</code>.

If a player connects to a new mob M, client.eye automatically changes to M.


```dm

client
  eye = locate(5,5,1)

```


This fixes the center of the player's map at the turf coordinate (5,5,1). Since the eye is fixed, the map will not scroll even as the player's mob moves out of the visible range.
***
**Related Pages:**
+    [edge_limit var (client)](/ref/client/var/edge_limit)
+    [lazy_eye var (client)](/ref/client/var/lazy_eye)
+    [mob var (client)](/ref/client/var/mob)
+    [perspective var (client)](/ref/client/var/perspective)
+    [glide_size var (client)](/ref/client/var/glide_size)
+    [view var (client)](/ref/client/var/view)
+    [virtual_eye var (client)](/ref/client/var/virtual_eye)
+    [view var (world)](/ref/world/var/view)
+    [step_x var (movable atom)](/ref/atom/movable/var/step_x)
+    [step_y var (movable atom)](/ref/atom/movable/var/step_y)
