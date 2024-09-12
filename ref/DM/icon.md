## icons



An icon file may be referenced by putting single quotes around
the filename. The file extension determines the type of icon. Currently
supported icon types are `.dmi`, `.bmp`, `.png`, `.jpg`, and `.gif`. To
create dmi icons, use the Dream Maker icon editor. This allows you to
make animations, 4 or 8 directional icons, and icons with different
states (such as \"live\" and \"dead\").
### Example:

```
 mob icon = \'monster.dmi\' 
```
 

You can also
load icons into memory at run-time and manipulate the graphical data to
produce new icons dynamically. This is done by creating an
[/icon](/ref/icon.md) object.

**See also:**
+   [FILE_DIR definition](/ref/DM/preprocessor/define/FILE_DIR.md) 
+   [cache](/ref/DM/cache.md) 
+   [flick proc](/ref/proc/flick.md) 
+   [icon](/ref/icon.md) 
+   [icon var (atom)](/ref/atom/var/icon.md) 
+   [icon_state var (atom)](/ref/atom/var/icon_state.md) 
+   [image objects](/ref/image.md) 