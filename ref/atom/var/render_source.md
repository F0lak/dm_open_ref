## render_source var (atom)
**See also:**
+   [render_target var (atom)](/ref/atom/var/render_target.md) 
+   [appearance_flags var (atom)](/ref/atom/var/appearance_flags.md) 
<!-- -->
**Default value:**
+   null
<!-- -->
**Possible values:**
+   Any non-empty text string


If any icon uses `render_source`, the renderer will look for
another icon with a matching `render_target` value on the visible map,
and draw that in place of the `icon`/`icon_state`/`dir` that it normally
would. The same render target might be used as a source multiple times,
and for a complex image this can save some rendering time. This is also
usable for special effects such as [filters](/ref/%7Bnotes%7D/filters.md)  that
might require copies of an image. 

Note+ The corresponding
`render_target` *must* be visible to the player for a render source to
be used. 

The replacement icon from the `render_source` will be
anchored to the bottom left of the icon it replaces. 

Other vars
that would normally affect the appearance of this icon, such as `color`,
`transform`, `filters`, `appearance_flags`, etc. are all applied.
Additionally, if this object has overlays, underlays, or visual
contents, those will still be drawn as well. 

Note+ Any mouse
hits on this object belong to the object itself, not to the object used
in the `render_source` or its children. If you want mouse clicks and
other behavior to go to the source, use the `PASS_MOUSE` [appearance
flag](/ref/atom/var/appearance_flags.md) 