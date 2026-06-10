
## generator (proc)

**Format:**
+   generator(type, A, B, rand)

**Arguments:**
+   type: The type of generator object, which determines what kind of results it produces
+   A: One extreme of the generator results
+   B: The other extreme
+   rand: Type of random distribution used
***
Creates a generator that can be used to produce a random value. This generator can be used in client-side particle effects, or it can be used in proc code. The types of values it can produce are numbers, 2D or 3D vectors, or colors (a text string like "#rrggbb" or a color matrix).
***
**Related Pages:**
+    [Generators](/ref/{notes}/generators)
+    [Particle effects](/ref/{notes}/particles)
+    [color var (atom)](/ref/atom/var/color)
+    [Color matrix](/ref/{notes}/color-matrix)
+    [vector](/ref/vector)
+    [stddef.dm file](/ref/{{appendix}}/stddef%2edm)
