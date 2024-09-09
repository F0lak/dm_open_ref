[]{#/{notes}/filters toc="Filter effects"}    
## Filter effects {#filter-effects byondver="512"}    
**See also:**    
:   [filters var (atom)](/ref/atom/var/filters/filters.md)    
:   [appearance_flags var (atom)](/ref/atom/var/appearance_flags/appearance_flags.md)    
:   [filter proc](/ref/proc/filter/filter.md)    
:   [animate proc](/ref/proc/animate/animate.md)    
:   [Understanding the renderer](/ref/%7Bnotes%7D/renderer/renderer.md)    
Filters are a way of adding special effects to an icon, or a group of    
icons (see `KEEP_TOGETHER` in    
[appearance_flags](/ref/atom/var/appearance_flags/appearance_flags.md){.code}), by    
post-processing the image. A filter object describes a specific form of    
image processing, like for instance a blur or a drop shadow. Filters can    
be added or removed at will, and can even be animated.    
A filter is created by using the [filter proc](/ref/proc/filter/filter.md) like so:    
// halo effect mob.filters += filter(type=\"drop_shadow\", x=0, y=0,\\    
size=5, offset=2, color=rgb(255,255,170))    
These are the filters currently supported:    
-   [Alpha mask](/ref/%7Bnotes%7D/filters/alpha/alpha.md)    
-   [Angular blur](/ref/%7Bnotes%7D/filters/angular_blur/angular_blur.md)    
-   [Bloom](/ref/%7Bnotes%7D/filters/bloom/bloom.md)    
-   [Color matrix](/ref/%7Bnotes%7D/filters/color/color.md)    
-   [Displacement map](/ref/%7Bnotes%7D/filters/displace/displace.md)    
-   [Drop shadow](/ref/%7Bnotes%7D/filters/drop_shadow/drop_shadow.md)    
-   [Gaussian blur](/ref/%7Bnotes%7D/filters/blur/blur.md)    
-   [Layering (composite)](/ref/%7Bnotes%7D/filters/layer/layer.md)    
-   [Motion blur](/ref/%7Bnotes%7D/filters/motion_blur/motion_blur.md)    
-   [Outline](/ref/%7Bnotes%7D/filters/outline/outline.md)    
-   [Radial blur](/ref/%7Bnotes%7D/filters/radial_blur/radial_blur.md)    
-   [Rays](/ref/%7Bnotes%7D/filters/rays/rays.md)    
-   [Ripple](/ref/%7Bnotes%7D/filters/ripple/ripple.md)    
-   [Wave](/ref/%7Bnotes%7D/filters/wave/wave.md)  