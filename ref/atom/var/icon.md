[]{#/icon var (atom).md}    
## icon var (atom)    
**See also:**    
:   [icon proc](/proc/icon)    
:   [icon_state var (atom)](/icon var (atom).md_state)    
:   [icons](/DM/icon)    
:   [overlays var (atom)](/atom/var/overlays)    
:   [underlays var (atom)](/atom/var/underlays)    
:   [load_resource proc](/proc/load_resource)    
:   [icon_w var (atom)](/icon var (atom).md_w)    
:   [icon_z var (atom)](/icon var (atom).md_z)    
<!-- -->    
**Default value:**    
:   null    
This is the icon file that will be used to represent the object on    
graphical clients.    
### Example:    
turf/wall icon = \'wall.dmi\'    
You can also assign this to an external file at run-time with an    
expression such as file(\"wall.dmi\"), but you would only want to do    
that when the other method is not possible, because it requires addition    
of the file to the resource cache, which can take a little time.    
When this variable is set to any dynamically created icon object, that    
object gets dumped into the world\'s resource cache (the `.rsc` file),    
and a reference to that cached file is assigned to atom.icon. In other    
words, don\'t expect comparisons such as    
`usr.icon == MyDynamicallyCreatedIcon` to work unless you have used    
fcopy_rsc() to get a cache reference to your dynamically created icon    
first. This is almost never an issue, so don\'t worry about it if none    
of that made any sense to you!  