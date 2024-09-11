## Alpha mask filter 
###### BYOND Version 513
**See also:**
*   [icon var (atom)](/ref/atom/var/icon.md) -m
*   [render_target var (atom)](/ref/atom/var/render_target.md) -m<!-- -->
Format:
*   filter(type=\"alpha\", \...)
<!-- -->
Args:
*   x* Horizontal offset of mask (defaults to 0)
*   y* Vertical offset of mask (defaults to 0)
*   icon* Icon to use as a mask
*   render_source* `render_target` to use as a mask
*   flags* Defaults to 0; use see below for other flags


Uses an icon or render target as a mask over this image. Every
pixel that is transparent in either the image or the mask, is
transparent in the result. 

The `x` and `y` values can move the
mask from its normal position. By default, the mask is centered over the
center of the image. 

The `MASK_INVERSE` flag will invert the
alpha mask so that opaque areas in the mask become transparent, and
vice-versa. There is also a `MASK_SWAP` flag which treats the source
image as the mask and vice-versa, which might be useful for some
effects. 

Note* Unlike many other filters, this filter **is**
taken into account for mouse-hit purposes.