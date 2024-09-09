[]{#/{skin}/param/zoom-mode}    
## zoom-mode parameter (skin) {#zoom-mode-parameter-skin byondver="511"}    
**See also:**    
:   [letterbox parameter](/ref/%7Bskin%7D/param/letterbox)    
:   [view-size parameter](/ref/%7Bskin%7D/param/view-size)    
:   [zoom parameter](/ref/%7Bskin%7D/param/zoom)    
<!-- -->    
**Applies to:**    
:   [Map](/ref/%7Bskin%7D/control/map)    
<!-- -->    
**Posisble values:**    
:   normal    
:   distort    
:   blur    
<!-- -->    
**Default value:**    
:   normal    
Controls the way the map is upscaled.    
normal    
Preserves a pixelated look, but does some blending between adjacent    
pixels when the zoom factor is not an integer. This is equivalent to    
upscaling by the next highest integer, then downscaling.    
distort    
Uses nearest-neighbor sampling to upscale. This may look odd if the zoom    
factor is not an integer, since for instance some pixels might scale up    
to be 2 pixels wide, others 3 pixels wide. Some users prefer it anyway.    
blur    
Uses bilinear sampling to upscale. This will cause a blurry appearance    
if the zoom factor is high, but it may be desired in some cases.  