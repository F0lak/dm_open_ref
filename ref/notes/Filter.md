[]{#/{notes}/filters toc="Filter effects"}
  ## Filter effects {#filter-effects byondver="512"}
  **See also:**
  :   [filters var (atom)](ref/atom/var/filters)
  :   [appearance_flags var (atom)](ref/atom/var/appearance_flags)
  :   [filter proc](ref/proc/filter)
  :   [animate proc](ref/proc/animate)
  :   [Understanding the renderer](ref/%7Bnotes%7D/renderer)
  Filters are a way of adding special effects to an icon, or a group of
  icons (see `KEEP_TOGETHER` in
  [appearance_flags](ref/atom/var/appearance_flags){.code}), by
  post-processing the image. A filter object describes a specific form of
  image processing, like for instance a blur or a drop shadow. Filters can
  be added or removed at will, and can even be animated.
  A filter is created by using the [filter proc](ref/proc/filter) like so:
  // halo effect mob.filters += filter(type=\"drop_shadow\", x=0, y=0,\\
  size=5, offset=2, color=rgb(255,255,170))
  These are the filters currently supported:
  -   [Alpha mask](ref/%7Bnotes%7D/filters/alpha)
  -   [Angular blur](ref/%7Bnotes%7D/filters/angular_blur)
  -   [Bloom](ref/%7Bnotes%7D/filters/bloom)
  -   [Color matrix](ref/%7Bnotes%7D/filters/color)
  -   [Displacement map](ref/%7Bnotes%7D/filters/displace)
  -   [Drop shadow](ref/%7Bnotes%7D/filters/drop_shadow)
  -   [Gaussian blur](ref/%7Bnotes%7D/filters/blur)
  -   [Layering (composite)](ref/%7Bnotes%7D/filters/layer)
  -   [Motion blur](ref/%7Bnotes%7D/filters/motion_blur)
  -   [Outline](ref/%7Bnotes%7D/filters/outline)
  -   [Radial blur](ref/%7Bnotes%7D/filters/radial_blur)
  -   [Rays](ref/%7Bnotes%7D/filters/rays)
  -   [Ripple](ref/%7Bnotes%7D/filters/ripple)
  -   [Wave](ref/%7Bnotes%7D/filters/wave)