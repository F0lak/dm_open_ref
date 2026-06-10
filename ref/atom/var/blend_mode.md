
## blend_mode (var)

**Default Value:**
+   0 (none/overlay)
***
[<small>*</small> This blend type appears only when using graphics hardware mode. It is also not visible in the map editor.]<br/> [<small>†</small> Since the alpha of the icon underneath is used for alpha masking, mouse hits take it into account.]

Controls the way the atom's icon is blended onto the icons behind it. The blend mode used by an atom is inherited by any attached overlays, unless they override it. `BLEND_DEFAULT` will use the main atom's blend mode; for the atom itself, it's the same as `BLEND_OVERLAY`.

`BLEND_OVERLAY` will draw an icon the normal way.

`BLEND_ADD` will do additive blending, so that the colors in the icon are added to whatever is behind it. Light effects like explosions will tend to look better in this mode.

`BLEND_SUBTRACT` is for subtractive blending. This may be useful for special effects.

`BLEND_MULTIPLY` will multiply the icon's colors by whatever is behind it. This is typically only useful for applying a colored light effect; for simply darkening, using a translucent black icon with normal overlay blending is a better option.

`BLEND_INSET_OVERLAY` overlays the icon, but masks it by the image being drawn on. This is pretty much not at all useful directly on the map, but can be very useful for an overlay for an atom that uses `KEEP_TOGETHER` (see <a class="code" href="#/atom/var/appearance_flags">appearance_flags</a>), or for the <a href="#/{notes}/filters/layer">layering filter</a>.
***
**Related Pages:**
+    [vars (atom)](/ref/atom/var)
+    [alpha](/ref/atom/var/alpha)
+    [color var (atom)](/ref/atom/var/color)
+    [appearance_flags var (atom)](/ref/atom/var/appearance_flags)
