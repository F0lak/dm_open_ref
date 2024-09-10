## Motion blur filter {#motion-blur-filter byondver="512"}    
**See also:**    
:   [filters var (atom)](/atom/var/filters)    
:   [Gaussian blur (filters)](/%7Bnotes%7D/filters/blur)    
<!-- -->    
Format:    
:   filter(type=\"motion_blur\", \...)    
<!-- -->    
Args:    
:   x: Blur vector on the X axis (defaults to 0)    
:   y: Blur vector on the Y axis (defaults to 0)    
Applies Gaussian blur in one direction only. The amount and direction    
are both specified by `x` and `y`. The size of the blur is equal to    
`sqrt(x*x + y*y)`.    
See [Gaussian blur](/%7Bnotes%7D/filters/blur) for more information.  