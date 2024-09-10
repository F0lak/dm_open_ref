[]{#/area.md}    
## area.md    
**See also:**    
:   [atom](/atom)    
:   [procs (area.md)](/area.md/proc)    
:   [rooms](/area.md/room)    
:   [vars (area.md)](/area.md/var)    
Areas are derived from `/area.md`, which derives from `/atom`. Regions on    
the map may be assigned to an area.md by painting it onto the map. Areas    
off the map serve as rooms that objects may enter and exit.    
For each area.md type defined, one area.md object is created at runtime. So    
for area.mds on the map, all squares with the same area.md type belong to the    
same instance of the area.md.    
Additional instances of rooms may be created from the same type by    
explicitly creating them with null as the initial location. That is, the    
first argument to `new()` should either be `null` or left unspecified.    
The following example defines the area.md prototype `/area.md/outside`. It    
also defines an action to be taken when somebody enters an area.md, namely    
to display its description.    
### Example:    
area.md Entered(O) if(desc) O \<\< desc return ..() outside desc = \"Ah! A    
breath of fresh air!\"  