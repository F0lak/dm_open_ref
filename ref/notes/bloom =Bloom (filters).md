## Bloom filter 
###### BYOND Version 514
**See also:**
*   [Gaussian blur (filters)](/%7Bnotes%7D/filters/blur)
*   [Drop shadow (filters)](/%7Bnotes%7D/filters/drop_shadow)
<!-- -->
Format:
*   filter(type=\"bloom\", \...)
<!-- -->
Args:
*   threshold* Color threshold for bloom
*   size* Blur radius of bloom effect (see Gaussian blur)
*   offset* Growth/outline radius of bloom effect before blur
*   alpha* Opacity of effect (default is 255, max opacity)


Post-processing effect that makes bright colors look like
they\'re a strong light source, spreading their light additively to
other nearby pixels. This is a complex effect that involves multiple
shader passes. For both performance and visual reasons, it is usually
best applied to an entire plane rather than to individual objects.


The color `threshold` determines which pixels this effect
applies to. If any of the red, green, or blue components of the pixel
are greater than the same component for the threshold, that pixel will
bloom. The blooming pixels then have their colors spread outward to
create a glow that gets added to the original image. 

The
`offset` and `size` parameters are used to control the glow effect. They
work the same as they do in the drop shadow filter* `offset` causes the
light to grow outwards, and a blur of `size` is then applied to soften
it. Often just using a blur alone will produce a pleasing effect. By
playing with these two values you can make the bloom effect appear
differently. 

The `alpha` value is applied to any light
contributions from bloomed pixels that get added to the original image,
so values lower than 255 can make the effect less pronounced. This can
be very useful if you choose to animate the filter.