## list associations    
**See also:**    
:   [list](/list)    
:   [list proc](/proc/list)    
:   [list proc](/proc/alist)    
:   [list2params proc](/proc/list2params)    
:   [params var (world)](/world/var/params)    
:   [params2list proc](/proc/params2list)    
:   [vars list var (datum)](/datum/var/vars)    
Each unique text string or object in a list may be associated with    
another value. This is done by using the item as an index into the list.    
### Example:    
var/params\[0\] params\[\"player\"\] = \"James Byond\"    
params\[\"score\"\] = 2000 //List now contains (\"player\",\"score\")    
//These are associated with (\"James Byond\",2000) usr \<\< \"Looping    
through list items:\" var/p for(p in params) usr \<\< \"\[p\] =    
\[params\[p\]\]\" usr \<\< \"Looping through array indices:\" var/i    
for(i=1,i\<=params.len,i++) p = params\[i\] usr \<\< \"\[p\] =    
\[params\[p\]\]\"    
The above example illustrates the typical way in which list associations    
are managed. Note that an item in the list may be added by assigning its    
associated value. The example could have started by doing    
`params.Add("player","score")`, but that would have been redundant.    
Both `for` loops in the example have the same effect. The first one    
loops through each item in the list, and displays it along with its    
associated value. The second loop achieves the same thing by looping    
through the numerical indices (referred to as *array* indices as opposed    
to *associative* indices).    
Since numeric indices are treated differently, accessing the Nth item in    
the list, you may not assign an associated value to a numeric list item.    
Associations must have a text string or object reference as the index    
item. (`alist()` is an exception to this, and can use numeric    
associations. See [alist()](/list/alist){.code} for more information.)    
Associated values default to null if none is assigned. This is also the    
value returned when the supplied index item does not exist in the list.    
The list defined above, for example, would return null for    
`params["time"]`.    
The [list()](/proc/list){.code} or [alist()](/proc/alist){.code}    
instructions may also be used to create associative lists.    
### Example:    
var/list/lst = list(\"player\" = \"James Byond\", \"score\" = 2000)    
When the index values happen to be text strings that satisfy all the    
requirements for variable names, this may also be written in a    
convenient short-hand: var/list/lst = list(player = \"James Byond\",    
score = 2000)    
In other words, this is exactly the same syntax as for [named    
arguments](/proc/arguments/named).    
The [`alist` proc](/proc/alist) creates lists that are *strictly*    
associative. This means that list items are treated as \"keys\" in    
key,value pairs. Unlike a regular list, each \"key\" is unique.  