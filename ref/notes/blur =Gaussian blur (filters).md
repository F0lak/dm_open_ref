[]{#/Gaussian blur filter.md}/filters/blur toc="Gaussian blur (filters)"}    
## Gaussian blur filter {#gaussian-blur-filter byondver="512"}    
**See also:**    
:   [Motion blur (filters)](/%7Bnotes%7D/filters/motion_blur)    
:   [Radial blur (filters)](/%7Bnotes%7D/filters/radial_blur)    
:   [Angular blur (filters)](/%7Bnotes%7D/filters/angular_blur)    
:   [Drop shadow (filters)](/%7Bnotes%7D/filters/drop_shadow)    
<!-- -->    
Format:    
:   filter(type=\"blur\", \...)    
<!-- -->    
Args:    
:   size: Amount of blur (defaults to 1)    
Blurs the image by a certain amount. The size of the blur can roughly be    
thought of in \"pixels\" worth of blur.    
Note: Large blurs will result in reduced performance. The highest size    
that can be handled easily in this filter is 6. Higher sizes require    
multiple passes, although the filter will \"cheat\" and use low-quality    
passes for much higher sizes.  