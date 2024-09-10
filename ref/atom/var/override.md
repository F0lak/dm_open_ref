## override var (atom)    
**Default value:**    
:   0    
**Currently this only applies to [images](/image).**    
If you attach an image to an atom, normally it is seen only in addition    
to the atom\'s regular icon. If the image\'s override var is 1, it will    
be seen *in place of* the original atom (and its overlays). It will    
inherit the atom\'s color, alpha, transform, and appearance_flags,    
unless its own appearance_flags say otherwise.    
If the image has a specific name and/or suffix value, those will    
override the parent atom too. Leaving them blank will let the original    
atom take precedence.  