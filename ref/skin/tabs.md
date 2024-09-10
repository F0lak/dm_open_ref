[]{#/tabs parameter (skin).md}/param/tabs}    
## tabs parameter (skin)    
**See also:**    
:   [current-tab parameter](/%7Bskin%7D/param/current-tab)    
:   [id parameter](/%7Bskin%7D/param/id)    
:   [multi-line parameter](/%7Bskin%7D/param/multi-line)    
<!-- -->    
**Applies to:**    
:   [Tab](/%7Bskin%7D/control/tab)    
<!-- -->    
**Format:**    
:   string    
A comma-separated list of [id](/%7Bskin%7D/param/id){.code} values for    
the panes included as tabs in this control.    
When setting this value, you can put `+` in front of the list to add    
tabs to the existing control, without affecting current tabs. You can    
likewise use `-` in front of the list to remove tabs.    
Note: When using this with [winset()](/proc/winset){.code}, remember    
you will need to escape `+` as `%2B` via    
[url_encode()](/proc/url_encode){.code} or    
[list2params()](/proc/list2params){.code}.  