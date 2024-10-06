# missile proc
**Format:**
+   missile(Type, Start, End)
<!-- -->
**Args:**
+   Type: An object prototype or icon file.
+   Start: The starting location.
+   End: The ending location.


Send a missile of the given Type between two locations. The
effect is purely visual. When Type is an object, its icon is used for
the missile.
### Example:

```dm
 missile(/obj/fireball, usr, loc) 
```
