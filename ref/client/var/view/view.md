[]{#/client/var/view}    
## view var (client)    
**See also:**    
:   [lazy_eye var (client)](ref/client/var/lazy_eye)    
:   [show_map var (client)](ref/client/var/show_map)    
:   [view proc](ref/proc/view)    
:   [view var (world)](ref/world/var/view)    
<!-- -->    
**Default value:**    
:   world.view (which is 5 by default)    
<!-- -->    
**Possible values:**    
:   -1 to 34 or \"WIDTHxHEIGHT\"    
This controls the size of the map window in Dream Seeker. Normally, you    
would simply compile with world/view assigned to whatever you want, but    
in some cases, you might want to customize the map size for different    
players, such as admins or subscribed users.    
Like all other view sizes in DM, this may either be a *view depth* or an    
absolute size. A view depth is a single number that determines how far    
from a center point the edges of a square viewable region extend. A    
value of 5 creates edges which are 2\*5+1 = 11 tiles long.    
The newer, more flexible syntax is a text string of the form    
\"WIDTHxHEIGHT\". For example, a view depth of 5 corresponds to    
\"11x11\". Using this syntax, you can create non-square views as well.    
The maximum view size is about 5000 tiles, or roughly 70x70.  