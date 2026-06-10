
## alpha (info)
***
Uses an icon or render target as a mask over this image. Every pixel that is transparent in either the image or the mask, is transparent in the result.

The `x` and `y` values can move the mask from its normal position. By default, the mask is centered over the center of the image.

The `MASK_INVERSE` flag will invert the alpha mask so that opaque areas in the mask become transparent, and vice-versa. There is also a `MASK_SWAP` flag which treats the source image as the mask and vice-versa, which might be useful for some effects.

Note: Unlike many other filters, this filter **is** taken into account for mouse-hit purposes.
***