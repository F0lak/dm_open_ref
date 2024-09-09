[]{#/{notes}/filters/radial_blur toc="Radial blur (filters)"}    
## Radial blur filter {#radial-blur-filter byondver="513"}    
**See also:**    
:   [Gaussian blur (filters)](/ref/%7Bnotes%7D/filters/blur)    
:   [Angular blur (filters)](/ref/%7Bnotes%7D/filters/angular_blur)    
:   [Motion blur (filters)](/ref/%7Bnotes%7D/filters/motion_blur)    
<!-- -->    
Format:    
:   filter(type=\"radial_blur\", \...)    
<!-- -->    
Args:    
:   x: Horizontal center of effect, in pixels, relative to image center    
:   y: Vertical center of effect, in pixels, relative to image center    
:   size: Amount of blur per pixel of distance (defaults to 0.01)    
Blurs the image by a certain amount outward from the center, as if the    
image is zooming in or out. As the distance from the center increases,    
the amount of blurring increases, and near the center the blur is hardly    
visible at all. The `size` value is smaller by default for this filter    
than it is for other filters, since it\'s typically used with an entire    
plane where the distance from the center can easily be several hundred    
pixels.    
Typically this blur is used with an entire plane.    
Note: Large blurs will look worse toward the edges due to limited    
sampling. Loss of accuracy will begin when `size` × distance is greather    
than 6. You can increase accuracy by breaking up large sizes into    
multiple filter passes. The blur used is Gaussian, so combining blur    
sizes A and B will give a total size of sqrt(A^2^+B^2^).  