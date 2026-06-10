
## contents (var)
***
This is a list of every object in the world. Objects in this list are in no particular order.


```dm

proc/ListAreas(mob/M)
  var/area/A
  M << "Areas:"
  for (A in world.contents)
    M << A

```


This example displays a list of every area in existence. As a convenient short-hand, one may simply write for(A) or for(A in world) instead of the full for(A in world.contents).
***