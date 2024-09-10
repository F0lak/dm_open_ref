## Scale proc (icon)    
**See also:**    
:   [icon](/icon)    
:   [procs (icon)](/icon/proc)    
:   [icon_size var (world)](/world/var/icon_size)    
:   [map_format var (world)](/world/var/map_format)    
:   [Big icons](/%7Bnotes%7D/big-icons)    
:   [Tiled icons](/%7Bnotes%7D/tiled-icons)    
<!-- -->    
**Format:**    
:   Scale(width, height)    
<!-- -->    
**Args:**    
:   width,height: size of the new icon    
The current icon is scaled to a new size.    
If world.map_format is set to TILED_ICON_MAP and the new size is not in    
multiples of world.icon_size, the icon will be padded with transparent    
pixels to the top and right as needed. See map_format for more    
information.    
Scale() automatically performs antialiasing to avoid unwanted artifacts.  