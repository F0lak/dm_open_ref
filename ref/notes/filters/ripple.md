
## ripple (info)
***
Applies a ripple distortion effect to this image.

This filter is meant to be animated. A good animation will typically start at a `radius` of 0 and animate to a larger value, with `size` decreasing to 0.

The `falloff` parameter can be tweaked to your liking. A value of 1 should look reasonably like ripples in water, with the inner ripples losing strength. A value of 0 will cause no reduction in strength.

The equation governing the ripple distortion is size × sin(2πr') ÷ (2.5 × falloff × r'<sup>2</sup> + 1), where r' = (radius - distance) ÷ repeat.

Up to 10 ripples can be stacked together in a single pass of the filter, as long as they have the same `repeat`, `falloff`, and `flags` values. (See the wave filter for the `WAVE_BOUNDED` flag.)
***