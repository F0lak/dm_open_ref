## Filter effects 
###### BYOND Version 512



Filters are a way of adding special effects to an icon, or a
group of icons (see `KEEP_TOGETHER` in
[appearance_flags](/ref/atom/var/appearance_flags.md) ), by
post-processing the image. A filter object describes a specific form of
image processing, like for instance a blur or a drop shadow. Filters can
be added or removed at will, and can even be animated. 

A filter
is created by using the [filter proc](/ref/proc/filter.md)  like so:

``` dm
 // halo effect mob.filters += filter(type="drop_shadow",
x=0, y=0,\\ size=5, offset=2, color=rgb(255,255,170)) 
```



These are the filters currently supported:
-   [Alpha mask](/ref/notes/filters/alpha.md) 
-   [Angular blur](/ref/notes/filters/angular_blur.md) 
-   [Bloom](/ref/notes/filters/bloom.md) 
-   [Color matrix](/ref/notes/filters/color.md) 
-   [Displacement map](/ref/notes/filters/displace.md) 
-   [Drop shadow](/ref/notes/filters/drop_shadow.md) 
-   [Gaussian blur](/ref/notes/filters/blur.md) 
-   [Layering (composite)](/ref/notes/filters/layer.md) 
-   [Motion blur](/ref/notes/filters/motion_blur.md) 
-   [Outline](/ref/notes/filters/outline.md) 
-   [Radial blur](/ref/notes/filters/radial_blur.md) 
-   [Rays](/ref/notes/filters/rays.md) 
-   [Ripple](/ref/notes/filters/ripple.md) 
-   [Wave](/ref/notes/filters/wave.md) 

> [!TIP] 
> **See also:**
> +   [filters var (atom)](/ref/atom/var/filters.md) 
> +   [appearance_flags var (atom)](/ref/atom/var/appearance_flags.md) 
> +   [filter proc](/ref/proc/filter.md) 
> +   [animate proc](/ref/proc/animate.md) 
> +   [Understanding the renderer](/ref/notes/renderer.md) 