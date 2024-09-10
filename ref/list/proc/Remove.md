## Remove proc (list)    
**See also:**    
:   [- operator](/operator/-)    
:   [Add proc (list)](/list/proc/Add)    
:   [RemoveAll proc (list)](/Remove proc (list).mdAll)    
<!-- -->    
**Format:**    
:   list.Remove(Item1,Item2,\...)    
<!-- -->    
**Returns:**    
:   1 if any items removed, 0 if not.    
<!-- -->    
**Args:**    
:   One or more items to remove from the list.    
Removes the specified items from the list. If an argument is itself a    
list, each item contained in it will be removed. Removal starts at the    
end of the list (highest index) so that this operation is an exact    
reversal of Add().  