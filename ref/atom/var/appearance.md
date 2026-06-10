
## appearance (var)
***
Every atom or image has an appearance, which controls all of the values relating to how it appears on the map. (The overlays and underlays lists are lists of appearances.) When read, this var provides a copy of the current appearance.

This value can also be used to change an atom's appearance, altering multiple values at once. Setting atom.appearance to another appearance will change all of the following values to match:

Other vars that are technically part of the appearance, but don't make any sense to change when cloning, are not changed. These include `density`, `dir`, `screen_loc`, and `verbs`. However, those vars ARE copied when you assign a `/mutable_appearance`.

If you set `atom.appearance` to another atom, the other atom's appearance will be copied.
***
**Related Pages:**
+    [vars (atom)](/ref/atom/var)
+    [mutable appearance](/ref/mutable_appearance)
+    [Understanding the renderer](/ref/{notes}/renderer)
