## Gaussian blur filter 
###### BYOND Version 512
**See also:**
*   [Motion blur (filters)](/ref/%7Bnotes%7D/filters/motion_blur.md) -m
*   [Radial blur (filters)](/ref/%7Bnotes%7D/filters/radial_blur.md) -m
*   [Angular blur (filters)](/ref/%7Bnotes%7D/filters/angular_blur.md) -m
*   [Drop shadow (filters)](/ref/%7Bnotes%7D/filters/drop_shadow.md) -m<!-- -->
Format:
*   filter(type=\"blur\", \...)
<!-- -->
Args:
*   size* Amount of blur (defaults to 1)


Blurs the image by a certain amount. The size of the blur can
roughly be thought of in \"pixels\" worth of blur.
Note* Large blurs will result in reduced performance. The highest size
that can be handled easily in this filter is 6. Higher sizes require
multiple passes, although the filter will \"cheat\" and use low-quality
passes for much higher sizes.