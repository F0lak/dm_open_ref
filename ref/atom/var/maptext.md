
## maptext (var)

**Default Value:**
+   null
***
This is optional text that will be displayed in the same position as the atom. If an atom has both an icon and maptext, the text will be displayed in front of the icon. Usually however, this is something that would be added to an overlay or image object, which can then be positioned with pixel offsets.

Map text is constrained to the bounds set by maptext_width and maptext_height, which default to a single icon in size. It can be offset by maptext_x and maptext_y.

Text can use HTML and CSS, mostly the same limited subset supported by regular text output, and different styles can be used in the same block of text. In addition, alpha colors can also be used, by specifying a color as #rrggbbaa instead of just #rrggbb. (Alpha transparency will be ignored when the map is drawn without hardware rendering, so anything below 50% opacity is not displayed in those cases.)

Maptext supports links with the `&lt;a&gt;` tag. Left-clicking on a link will follow the link, but also generate other events such as `MouseDown` or `Click`.
***
**Related Pages:**
+    [maptext_width](/ref/atom/var/maptext_width)
+    [maptext_height](/ref/atom/var/maptext_height)
+    [maptext_x](/ref/atom/var/maptext_x)
+    [maptext_y](/ref/atom/var/maptext_y)
+    [overlays](/ref/atom/var/overlays)
+    [image objects](/ref/image)
+    [pixel_x](/ref/atom/var/pixel_x)
+    [pixel_y](/ref/atom/var/pixel_y)
+    [pixel_w var (atom)](/ref/atom/var/pixel_w)
+    [pixel_z var (atom)](/ref/atom/var/pixel_z)
