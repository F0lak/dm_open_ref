
## rays (info)
***
Draws random rays that radiate outward from a center point. (That point may be outside of the image.) As they move outward, their alpha value diminishes linearly. These are meant to be animated. The `offset` value determines the "time", where every jump of +1 can be a very different set of rays, and every 1000 units this filter will repeat.

The `threshold` value can be thought of as a way of culling lower-strength rays. Ray strength is anywhere from 0 to 1 at any given angle, but values below `threshold` may as well be 0. Values above that are re-scaled into a range of 0 to 1.

The `factor` parameter allows you to tie the ray's length to its strength. At 0, the length of every ray is the same. At 1, the length ranges from 0 to `size`. Generally speaking, the higher `factor` is, the more the rays will appear to move outward as they strengthen and inward as they weaken.

Ray `color` can be provided as a matrix. Only the diagonal values of the color matrix will be used, but using a matrix will allow you to set values outside of the normal color range.

`flags` can have the following values:
***