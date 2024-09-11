## vis_locs var (atom) 
###### BYOND Version 512
**See also:**
*   [vis_contents var (atom)](/atom/var/vis_contents)
*   [vis_flags var (atom)](/atom/var/vis_flags)
*   [image objects](/image)
*   [HUD / screen objects](/%7Bnotes%7D/HUD)
<!-- -->
**Default value:**
*   Empty list.


This list is the opposite of the `vis_contents` list. If this
atom is in any other atoms\' visual contents, those parent atoms will
appear in this list. 

Because only turfs, objs, and mobs can be
in visual contents, this var belongs only to those types. 

Being
in a visual locs list does not count as a [reference](/DM/garbage), the
same way that being a movable\'s loc does not count as a reference. If
an object in this list otherwise runs out of references, it will be
garbage collected and therefore removed from this list.