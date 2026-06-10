
## pixloc (info)
***
A primitive type that encapsulates position information for an atom, with pixel movement included. I.e., it contains a turf (loc) and step_x and step_y offsets. Pixlocs can also be built from absolute world coordinates.

The pixloc of an atom is taken from its loc and step_x/y vars only. If you want the pixloc of its bounds edges or its center, use the <a href="#/proc/bound_pixloc">`bound_pixloc()` proc</a> for that.

Pixlocs support some math operations. A <a href="#/vector">vector</a> can be added or subtracted to a pixloc, and subtracting one pixloc from another will produce a vector. The <a class="code" href="#/operator/%25">%</a> and <a class="code" href="#/operator/%25%25">%%</a> operators are supported, returning a vector.

Other supported procs for pixlocs include:
***
**Related Pages:**
+    [vars (pixloc)](/ref/pixloc/var)
+    [pixloc](/ref/atom/var/pixloc)
+    [pixloc proc](/ref/proc/pixloc)
+    [bound_pixloc proc](/ref/proc/bound_pixloc)
