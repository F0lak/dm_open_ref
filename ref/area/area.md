[]{#/area}    
## area    
**See also:**    
:   [atom](ref/atom)    
:   [procs (area)](ref/area/proc)    
:   [rooms](ref/area/room)    
:   [vars (area)](ref/area/var)    
Areas are derived from `/area`, which derives from `/atom`. Regions on    
the map may be assigned to an area by painting it onto the map. Areas    
off the map serve as rooms that objects may enter and exit.    
For each area type defined, one area object is created at runtime. So    
for areas on the map, all squares with the same area type belong to the    
same instance of the area.    
Additional instances of rooms may be created from the same type by    
explicitly creating them with null as the initial location. That is, the    
first argument to `new()` should either be `null` or left unspecified.    
The following example defines the area prototype `/area/outside`. It    
also defines an action to be taken when somebody enters an area, namely    
to display its description.    
### Example:    
area Entered(O) if(desc) O \<\< desc return ..() outside desc = \"Ah! A    
breath of fresh air!\"  