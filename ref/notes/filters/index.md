
## filters (info)
***
Filters are a way of adding special effects to an icon, or a group of icons (see `KEEP_TOGETHER` in <a class="code" href="#/atom/var/appearance_flags">appearance_flags</a>), by post-processing the image. A filter object describes a specific form of image processing, like for instance a blur or a drop shadow. Filters can be added or removed at will, and can even be animated.

A filter is created by using the <a href="#/proc/filter">filter proc</a> like so:


```dm

// halo effect
mob.filters += filter(type="drop_shadow", x=0, y=0,\
                      size=5, offset=2, color=rgb(255,255,170))

```


These are the filters currently supported:
***