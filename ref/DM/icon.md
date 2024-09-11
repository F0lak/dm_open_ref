## icons
**See also:**
*   [FILE_DIR definition](/DM/preprocessor/define/FILE_DIR)
*   [cache](/DM/cache)
*   [flick proc](/proc/flick)
*   [icon](/icon)
*   [icon var (atom)](/atom/var/icon)
*   [icon_state var (atom)](/atom/var/icon_state)
*   [image objects](/image)


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
[/icon](/icon) object.