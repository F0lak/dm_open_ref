## Angular blur filter 
###### BYOND Version 513
**See also:**
*   [Gaussian blur (filters)](/ref/%7Bnotes%7D/filters/blur.md) -m
*   [Radial blur (filters)](/ref/%7Bnotes%7D/filters/radial_blur.md) -m
*   [Motion blur (filters)](/ref/%7Bnotes%7D/filters/motion_blur.md) -m<!-- -->
Format:
*   filter(type=\"angular_blur\", \...)
<!-- -->
Args:
*   x* Horizontal center of effect, in pixels, relative to image center
*   y* Vertical center of effect, in pixels, relative to image center
*   size* Amount of blur (defaults to 1)


Blurs the image by a certain amount in a circular formation, as
if the image is spinning. The size of the blur can roughly be thought of
in \"degrees\" worth of blur. As the distance from the center increases,
the blur becomes more noticeable since the same amount of angular motion
has to travel farther along a circle. 

Typically this blur is
used with an entire plane, but it could be used to give a sense of
motion blur to a spinning object. 

Note* Large blurs will look
worse toward the edges due to limited sampling. Loss of accuracy will
appear where `size` × distance is greater than about 300. You can
increase accuracy by breaking up large sizes into multiple filter passes
with differing sizes. The blur used is Gaussian, so combining blur sizes
A and B will give a total size of sqrt(A^2^+B^2^).