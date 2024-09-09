[]{#/list/proc/Swap}    
## Swap proc (list)    
**See also:**    
:   [Cut proc (list)](/ref/list/proc/Cut.md)    
:   [Copy proc (list)](/ref/list/proc/Copy.md)    
:   [Insert proc (list)](/ref/list/proc/Insert.md)    
<!-- -->    
**Format:**    
:   list.Swap(Index1,Index2)    
<!-- -->    
**Returns:**    
:   Nothing.    
<!-- -->    
**Args:**    
:   Index1: The index (1 to list.len) of one of the items to swap.    
:   Index2: The index of the other item.    
Swap two items in a list. If the list has associated values, they will    
be preserved. This is most useful for user-defined sorting routines.    
### Example:    
var/item var/list/L = list(\"orange\" = 3, \"green\" = 2, \"blue\" = 5)    
for(item in L) world \<\< \"\[item\] -\> \[L\[item\]\]\" world \<\< \"\"    
L.Swap(1, 3) for(item in L) world \<\< \"\[item\] -\> \[L\[item\]\]\"    
### Result:    
orange -\> 3 green -\> 2 blue -\> 5 blue -\> 5 green -\> 2 orange -\> 3    
Note: This proc doesn\'t work with many special lists such as `contents`    
or `overlays`.  