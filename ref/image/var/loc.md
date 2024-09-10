## loc var (image)    
The location of an image specifies the object to which the image is    
attached. Unless the image drawing layer is specified, the default will    
make it appear above this object, as though it were an overlay.    
Note that the image is not *inside* the specified location. In other    
words, this loc variable does not behave like /atom/movable/var/loc    
which specifies the container object. It is more like the image is on    
top of the specified object. If the object moves, the image will    
automatically move around with it.  