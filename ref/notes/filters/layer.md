
## layer (info)
***
Composites another image over or under this image. Using the `FILTER_OVERLAY` flag, which is the default, puts the second image on top of what's already here. `FILTER_UNDERLAY` puts it underneath.

The `x` and `y` values can move the mask from its normal position. By default, the second image is centered over the center of the first.

The `color`, `transform`, and `blend_mode` vars are available for convenience. Because the bottom image is drawn over a blank background, `blend_mode` is always applied to the top image. All of the other vars apply to the second image being drawn.

Note: Transforms use default bilinear scaling, since <a class="code" href="#/atom/var/appearance_flags">PIXEL_SCALE</a> is not available here.

Note: Like most other filters, this filter is **not** taken into account for mouse-hit purposes. Any layered icons will be strictly visual.
***