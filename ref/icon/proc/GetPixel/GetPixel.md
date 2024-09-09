[]{#/icon/proc/GetPixel}    
## GetPixel proc (icon)    
**See also:**    
:   [icon](/ref/icon)    
:   [procs (icon)](/ref/icon/proc)    
:   [rgb proc](/ref/proc/rgb)    
<!-- -->    
**Format:**    
:   GetPixel(x, y, icon_state, dir=0, frame=0, moving=-1)    
<!-- -->    
**Args:**    
:   x,y: coordinates of the pixel to grab; 1,1 is the lower left corner    
:   icon_state: a specific icon_state to use (may be null)    
:   dir: a specific direction of this icon to use    
:   frame: a specific animation frame to use (1 is the 1st frame)    
:   moving: non-zero for only movement states, 0 for non-movement    
    states, or null (default) for either    
This finds the icon_state and the right animation/direction frame of    
your choosing (it will pick the first one available if you don\'t    
specify) and returns the rgb() value of a pixel at that location, in    
\"#RRGGBB\" form. If the pixel is totally transparent, it returns null.    
If the pixel is partially transparent, an alpha component is also    
returned in \"#RRGGBBAA\" form.  