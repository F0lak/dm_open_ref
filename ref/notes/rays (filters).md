# Rays filter 
###### BYOND Version 513
Format:
+   filter(type=\"rays\", \...)
<!-- -->
Args:
+   x: Horiztonal position of ray center, relative to image center
    (defaults to 0)
+   y: Vertical position of ray center, relative to image center
    (defaults to 0)
+   size: Maximum length of rays (defaults to 1/2 tile width)
+   color: Ray color (defaults to white)
+   offset: \"Time\" offset of rays (defaults to 0, repeats after 1000)
+   density: Higher values mean more, narrower rays (defaults to 10,
    must be whole number)
+   threshold: Low-end cutoff for ray strength (defaults to 0.5, can be
    0 to 1)
+   factor: How much ray strength is related to ray length (defaults to
    0, can be 0 to 1)
+   flags: Defaults to `FILTER_OVERLAY | FILTER_UNDERLAY` (see below)


Draws random rays that radiate outward from a center point.
(That point may be outside of the image.) As they move outward, their
alpha value diminishes linearly. These are meant to be animated. The
`offset` value determines the \"time\", where every jump of +1 can be a
very different set of rays, and every 1000 units this filter will
repeat. 

The `threshold` value can be thought of as a way of
culling lower-strength rays. Ray strength is anywhere from 0 to 1 at any
given angle, but values below `threshold` may as well be 0. Values above
that are re-scaled into a range of 0 to 1. 

The `factor`
parameter allows you to tie the ray\'s length to its strength. At 0, the
length of every ray is the same. At 1, the length ranges from 0 to
`size`. Generally speaking, the higher `factor` is, the more the rays
will appear to move outward as they strengthen and inward as they
weaken. 

Ray `color` can be provided as a matrix. Only the
diagonal values of the color matrix will be used, but using a matrix
will allow you to set values outside of the normal color range.


`flags` can have the following values:
0
+   The rays are drawn alone, erasing the existing image (useful for
    some effects).
FILTER_OVERLAY
+   The rays are overlaid on top of the existing image.
FILTER_UNDERLAY
+   The rays are drawn underneath the existing image.
FILTER_OVERLAY \| FILTER_UNDERLAY
+   Default. For plane masters, this will use the `FILTER_OVERLAY`
    behavior and draw the rays over the plane, and for all other images
    it will default to `FILTER_UNDERLAY` to draw the rays beneath them.