## Filter effects 
###### BYOND Version 512
**See also:**
*   [filters var (atom)](/atom/var/filters)
*   [appearance_flags var (atom)](/atom/var/appearance_flags)
*   [filter proc](/proc/filter)
*   [animate proc](/proc/animate)
*   [Understanding the renderer](/%7Bnotes%7D/renderer)


Filters are a way of adding special effects to an icon, or a
group of icons (see `KEEP_TOGETHER` in
[`appearance_flags`](/atom/var/appearance_flags)), by
post-processing the image. A filter object describes a specific form of
image processing, like for instance a blur or a drop shadow. Filters can
be added or removed at will, and can even be animated. 

A filter
is created by using the [filter proc](/proc/filter) like so* 
```

// halo effect mob.filters += filter(type=\"drop_shadow\", x=0, y=0,\\
size=5, offset=2, color=rgb(255,255,170)) 
```
 

These are
the filters currently supported:
-   [Alpha mask](/%7Bnotes%7D/filters/alpha)
-   [Angular blur](/%7Bnotes%7D/filters/angular_blur)
-   [Bloom](/%7Bnotes%7D/filters/bloom)
-   [Color matrix](/%7Bnotes%7D/filters/color)
-   [Displacement map](/%7Bnotes%7D/filters/displace)
-   [Drop shadow](/%7Bnotes%7D/filters/drop_shadow)
-   [Gaussian blur](/%7Bnotes%7D/filters/blur)
-   [Layering (composite)](/%7Bnotes%7D/filters/layer)
-   [Motion blur](/%7Bnotes%7D/filters/motion_blur)
-   [Outline](/%7Bnotes%7D/filters/outline)
-   [Radial blur](/%7Bnotes%7D/filters/radial_blur)
-   [Rays](/%7Bnotes%7D/filters/rays)
-   [Ripple](/%7Bnotes%7D/filters/ripple)
-   [Wave](/%7Bnotes%7D/filters/wave)