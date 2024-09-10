[]{#/Join proc (list).md}    
## Join proc (list) {#join-proc-list byondver="510"}    
**See also:**    
:   [jointext proc](/proc/jointext)    
<!-- -->    
**Format:**    
:   list.Join(Glue,Start=1,End=0)    
<!-- -->    
**Returns:**    
:   A text string made up of the items in this list, joined together by    
    Glue.    
<!-- -->    
**Args:**    
:   Glue: The text that will go between each item.    
:   Start: The list item on which to begin.    
:   End: The list item immediately following the last item to be joined.    
This is exactly the same as calling jointext(List,Glue,Start,End), and    
is provided for convenience.  