
## desc (var)

**Default Value:**
+   null
***
This is the description of the object.


```dm

mob/verb/look(atom/O in view())
   if(O.desc) usr << O.desc
   else usr << "It's just \an [O]."

```

***