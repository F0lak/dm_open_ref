
## edge_limit (var)

**Default Value:**
+   null
***
This value determines the limits that a client's eye will display. If <code>client.perspective</code> uses the <code>EDGE_PERSPECTIVE</code> flag, the view shouldn't scroll beyond the bounds set by <code>edge_limit</code>. If the bounds of <code>edge_limit</code> are as big as or smaller than the client's view, no scrolling will occur even if <code>EDGE_PERSPECTIVE</code> is not used. Normally this value is null, which provides freedom for the eye to move anywhere on the map. It may be changed to a text value describing the limits in more detail.

The format is similar to <code>atom.screen_loc</code> which uses <code>"[x1],[y1] to [x2],[y2]"</code>. It can also use directions such as <code>"SOUTHWEST to NORTHEAST"</code>, which refer to the limits of the map.


```dm

area/house
  var/x1,x2,y1,y2

  Entered(mob/M)
    if(ismob(M) && M.client)
      M.client.edge_limit = "[x1],[y1] to [x2],[y2]"

  Exited(mob/M)
    if(ismob(M) && M.client)
      M.client.edge_limit = null

```

***
**Related Pages:**
+    [eye var (client)](/ref/client/var/eye)
+    [lazy_eye var (client)](/ref/client/var/lazy_eye)
+    [perspective var (client)](/ref/client/var/perspective)
+    [view var (client)](/ref/client/var/view)
+    [screen_loc var (movable atoms)](/ref/atom/movable/var/screen_loc)
