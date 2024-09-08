[]{#/{notes}/filters/layer toc="Layering / composite (filters)"}
## Layering (composite) filter {#layering-composite-filter byondver="513"}
**See also:**
:   [icon var (atom)](#/atom/var/icon)
:   [render_target var (atom)](#/atom/var/render_target)
<!-- -->
Format:
:   filter(type=\"layer\", \...)
<!-- -->
Args:
:   x: Horizontal offset of second image (defaults to 0)
:   y: Vertical offset of second image (defaults to 0)
:   icon: Icon to use as a second image
:   render_source: `render_target` to use as a second image
:   flags: `FILTER_OVERLAY` (default) or `FILTER_UNDERLAY`
:   color: [Color](#/atom/var/color) or color matrix to apply to second
    image
:   transform: [Transform](#/atom/var/transform) to apply to second
    image
:   blend_mode: [Blend mode](#/atom/var/blend_mode) to apply to the top
    image
Composites another image over or under this image. Using the
`FILTER_OVERLAY` flag, which is the default, puts the second image on
top of what\'s already here. `FILTER_UNDERLAY` puts it underneath.
The `x` and `y` values can move the mask from its normal position. By
default, the second image is centered over the center of the first.
The `color`, `transform`, and `blend_mode` vars are available for
convenience. Because the bottom image is drawn over a blank background,
`blend_mode` is always applied to the top image. All of the other vars
apply to the second image being drawn.
Note: Transforms use default bilinear scaling, since
[PIXEL_SCALE](#/atom/var/appearance_flags){.code} is not available here.
Note: Like most other filters, this filter is **not** taken into account
for mouse-hit purposes. Any layered icons will be strictly visual.